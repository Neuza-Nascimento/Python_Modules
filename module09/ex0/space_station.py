#!/usr/bin/env python3

from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class Space_Station(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("==" * 20)
    try:
        space1 = Space_Station(
                station_id="ISS001",
                name="International Space Station",
                crew_size=6,
                power_level=85.5,
                oxygen_level=92.3,
                last_maintenance=datetime(2000, 2, 12),
                is_operational=True,
                notes="Wi-fi free"
        )

        print("Valid station created:")
        print(f"ID: {space1.station_id}")
        print(f"Name: {space1.name}")
        print(f"Crew: {space1.crew_size}")
        print(f"Power: {round(space1.power_level, 2)}%")
        print(f"Oxygen: {round(space1.oxygen_level, 2)}%")
        print("Status: ", end="")
        if space1.is_operational:
            print("Non ", end="")
        print("Operational\n")
        print("==" * 20)

        Space_Station(
                station_id="ISS002",
                name="Invalid Space Station",
                crew_size=30,
                power_level=85.5,
                oxygen_level=92.3,
                last_maintenance=datetime(2005, 3, 10),
        )
    except ValidationError as e:
        print("Expected validation error:\n")
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
