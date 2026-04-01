import random
from typing import Generator

PLAYERS = ['alice', 'bob', 'charlie', 'dylan']
ACTIONS = ['run', 'eat', 'sleep', 'grab', 'move', 'climb', 'swim',
           'use', 'release', 'jump']


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(events: list[tuple[str, str]]
                  ) -> Generator[tuple[str, str], None, None]:
    while events:
        event = random.choice(events)
        events.remove(event)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    generator = gen_event()

    for i in range(1000):
        name, action = next(generator)
        print(f"Event {i}: Player {name} did action {action}")

    events = []
    for _ in range(10):
        value = next(generator)
        events.append(value)

    print("Built list of 10 events:", events)
    consume_gen = consume_event(events)

    for event in consume_gen:
        print("Got event from list:", event)
        print("Remains in list:", events)


if __name__ == "__main__":
    main()
