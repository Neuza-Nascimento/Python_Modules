from pydantic import BaseModel, Field, ValidationError, model_validator
from typing_extensions import Self
from datetime import datetime
from typing import Optional, Any
from enum import Enum


class ContactType(str, Enum):
    # Types of contact
    RADIO = "radio"
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
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validation_regulament(self) -> Self:

        # Rule 1: Contact ID must start with "AC" (Alien Contact)
        if not self.contact_id.startswith("AC"):
            raise ValueError("\033[0;31m[KO]\033[0m "
                             "Contact ID must start with 'AC'")

        # Rule 2: Physical contact reports must be verified
        if (self.contact_type == ContactType.PHYSICAL
           and not self.is_verified):
            raise ValueError("\033[0;31m[KO]\033[0m "
                             "Physical Contact reports must be verified")

        # Rule 3: Telepathic contact requires at least 3 witnesses
        if (self.contact_type == ContactType.TELEPATHIC
           and not self.witness_count > 2):
            raise ValueError("\033[0;31m[KO]\033[0m "
                             "Telepathic contact requeried at least "
                             "3 witnesses")

        # Rule 4: Strong signals (> 7.0) should include received messages
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("\033[0;31m[KO]\033[0m "
                             "Strong signals (> 7.0) should include "
                             "received messages")
        return self


def create_alien(data: dict[str, Any]) -> AlienContactModel | None:

    try:
        return AlienContactModel(**data)

    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])

    return None


def show_alien(alien: AlienContactModel) -> None:

    data = alien.model_dump()
    for info in data:
        print(f"\033[0;37m • {info}:\033[0m "
              f"{data[info]}")


def print_title(msg: str) -> None:

    print(f"\033[1;38;5;178m{msg}\033[0m")


def main() -> None:
    print_title("\nAlien Contact Log Validation:")

    print("\n\033[1;37mAlien [1]\033[0m")

    data_1 = {
            "contact_id": "AC968470439",
            "timestamp": datetime(2003, 1, 31, 13, 30, 0, 0),
            "location": "BragaCity",
            "contact_type": "radio",
            "signal_strength": 7.5,
            "duration_minutes": 382,
            "witness_count": 5,
            "message_received": "all good",
            "is_verified": True,
            }

    alien_1 = create_alien(data_1)
    if alien_1:
        show_alien(alien_1)

    print("\n\033[1;37mAlien [2]\033[0m")

    data_2 = {
            "contact_id": "968470439",
            "timestamp": datetime(2003, 1, 31, 13, 30, 0, 0),
            "location": "BragaCity",
            "contact_type": "tmn",
            "signal_strength": 7.5,
            "duration_minutes": 382,
            "witness_count": 5,
            "message_received": "all good",
            "is_verified": True,
            }

    alien_2 = create_alien(data_2)
    if alien_2:
        show_alien(alien_2)

    print("\n\033[1;37mAlien [3]\033[0m")

    data_3 = {
            "contact_id": "AC968470439",
            "timestamp": datetime(2003, 1, 31, 13, 30, 0, 0),
            "location": "BragaCity",
            "contact_type": "physical",
            "signal_strength": 7.5,
            "duration_minutes": 382,
            "witness_count": 5,
            "message_received": "all good",
            "is_verified": False,
            }

    alien_3 = create_alien(data_3)
    if alien_3:
        show_alien(alien_3)

    print("\n\033[1;37mAlien [4]\033[0m")

    data_4 = {
            "contact_id": "AC968470439",
            "timestamp": datetime(2003, 1, 31, 13, 30, 0, 0),
            "location": "BragaCity",
            "contact_type": "telepathic",
            "signal_strength": 7.5,
            "duration_minutes": 382,
            "witness_count": 1,
            "message_received": "all good",
            "is_verified": True,
            }

    alien_4 = create_alien(data_4)
    if alien_4:
        show_alien(alien_4)


if __name__ == "__main__":
    main()