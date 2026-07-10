#!/usr/bin/env python3

from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime
from typing import Optional
from typing_extensions import Self


class ContactType(str, Enum):
    RADIO = "radio",
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContactModel(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validation_regulament(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError("The ID requires to start with "
                             "'AC'- Alien Contact")

        if (self.contact_type == ContactType.PHYSICAL
           and self.is_verified is False):
            raise ValueError("Physical contact reports must be verified")

        if (self.contact_type == ContactType.TELEPATHIC
           and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")

        if self.signal_strength < 0.7 and self.message_received is None:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages")

        return self


def print_alien_contact(alien: AlienContactModel) -> None:
    print("Valid contact report:")
    print(f"ID: {alien.contact_id}")
    print(f"Type: {alien.contact_type}")
    print(f"Location: {alien.location}")
    print(f"Signal: {alien.signal_strength}")
    print(f"Duration: {alien.duration_minutes} minutes")
    print(f"Witnesses: {alien.witness_count}")
    if alien.message_received is not None:
        print(f"Message: '{alien.message_received}'")
    print("==" * 20)


def main() -> None:
    print("Alien Contact Log Validation")
    print("==" * 20)
    try:
        alien1 = AlienContactModel(
                contact_id="AC_2024_002",
                timestamp=datetime(2000, 6, 2, 20, 30, 0),
                location="Area 51",
                contact_type=ContactType.RADIO,
                signal_strength=8.5,
                duration_minutes=45,
                witness_count=5,
                message_received=None,
                is_verified=False,
        )
        print_alien_contact(alien1)
    except ValidationError as e:
        print("Expected validation error:\n")
        for error in e.errors():
            print(error["msg"])

    try:
        alien2 = AlienContactModel(
                contact_id="AC_2024_002",
                timestamp=datetime(2005, 12, 25),
                location="Roswell",
                contact_type=ContactType.TELEPATHIC,
                signal_strength=6.2,
                duration_minutes=30,
                witness_count=1,
                message_received=None,
                is_verified=False
        )
        print_alien_contact(alien2)
    except ValidationError as e:
        print("Expected validation error:\n")
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
