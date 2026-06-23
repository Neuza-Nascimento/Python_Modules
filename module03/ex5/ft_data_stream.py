#!/usr/bin/python3

import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    achievements = [
        "Crafting Genius", "World Savior", "Master Explorer",
        "Collector Supreme", "Untouchable",
        "Boss Slayer", "Strategist", "Unstoppable", "Speed Runner",
        "Survivor", "Treasure Hunter", "First Steps", "Sharp Mind"
    ]
    names = ["Alice", "Charlie", "Bob", "Dylan"]
    while True:
        achievement = random.choice(achievements)
        name = random.choice(names)
        yield name, achievement


def consume_event(events: list[tuple[str, str]]) -> typing.Generator[
            tuple[str, str], None, None]:
    while (len(events) > 0):
        event = random.choice(events)
        events.remove(event)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    info = gen_event()
    for i in range(0, 1000):
        name, achivemnt = next(info)
        print(f"Event {i}: Player {name} did action {achivemnt} ")
    events = []
    for i in range(0, 10):
        events.append(next(info))
    print(f"Built of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")
    return


if __name__ == "__main__":
    main()
