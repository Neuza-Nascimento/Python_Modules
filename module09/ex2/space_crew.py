#!/usr/bin/env python3

from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime
from typing_extensions import Self
from typing import Any


class Rank(str, Enum):
    CADET = "cadet",
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMIssion(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember]
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validation_regulament(self) -> Self:

        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        if (not any(member.rank == Rank.CAPTAIN for member in self.crew)
           and not any(member.rank == Rank.COMMANDER for member in self.crew)):
            raise ValueError("Must have at least one Commander or Captain")

        if (self.duration_days > 365
           and not all([crew.years_experience > 5 for crew in self.crew])):
            raise ValueError("Long missions (> 365 days) need 50% "
                             "experienced crew (5+ years)")

        if not all(crew.is_active is True for crew in self.crew):
            raise ValueError("All crew members must be active")

        return self


def create_mission(space_mission: dict[str, Any]) -> SpaceMIssion | None:
    try:
        mission = SpaceMIssion.model_validate(space_mission)
        return mission
    except ValidationError as e:
        for error in e.errors():
            print("Expected validation error:")
            print(error["msg"])
        return None


def print_mission(mission: SpaceMIssion) -> None:
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${round(mission.budget_millions, 1)}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank}) - {member.specialization}")
    print()
    print("==" * 20)


def main() -> None:
    print("Space Mission Crew Validation")
    print("==" * 20)
    mission1_data = {
        'mission_id': 'M2024_TITAN',
        'mission_name': 'Solar Observatory Research Mission',
        'destination': 'Solar Observatory',
        'launch_date': '2024-03-30T00:00:00',
        'duration_days': 451,
        'crew': [
            {
                'member_id': 'CM001',
                'name': 'Sarah Williams',
                'rank': 'captain',
                'age': 43,
                'specialization': 'Mission Command',
                'years_experience': 19,
                'is_active': True
            },
            {
                'member_id': 'CM002',
                'name': 'James Hernandez',
                'rank': 'captain',
                'age': 43,
                'specialization': 'Pilot',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM003',
                'name': 'Anna Jones',
                'rank': 'cadet',
                'age': 35,
                'specialization': 'Communications',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM004',
                'name': 'David Smith',
                'rank': 'commander',
                'age': 27,
                'specialization': 'Security',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM005',
                'name': 'Maria Jones',
                'rank': 'cadet',
                'age': 55,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 2208.1
    }
    mission1: SpaceMIssion | None = create_mission(mission1_data)
    if mission1:
        print_mission(mission1)

    mission2_data = {
        'mission_id': 'M2027_TITAN',
        'mission_name': 'Luar Observatory Research Mission',
        'destination': 'Luar Observatory',
        'launch_date': '2027-10-25T00:00:00',
        'duration_days': 500,
        'crew': [
            {
                'member_id': 'CM003',
                'name': 'Anna Jones',
                'rank': 'cadet',
                'age': 35,
                'specialization': 'Communications',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM005',
                'name': 'Maria Jones',
                'rank': 'cadet',
                'age': 55,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 2080.1
    }

    mission2: SpaceMIssion | None = create_mission(mission2_data)
    if mission2:
        print_mission(mission2)


if __name__ == "__main__":
    main()
