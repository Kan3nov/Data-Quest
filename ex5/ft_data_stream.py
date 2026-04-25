import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str]]:
    players = ["bob", "alice", "dylan", "charlie", "meow"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim"]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(events: list) -> Generator[str, str]:
    while True:
        if (len(events) == 0):
            break
        idx = random.randint(0, len(events) - 1)
        event = events[idx]
        del events[idx]
        yield event


def main():
    print("=== Game Data Stream Processor ===")
    gen = gen_event()
    for x in range(1000):
        p, a = next(gen)
        print(f"Event {x}: Player {p} did action {a}")
    events = []
    for x in range(10):
        events.append(next(gen))
    print()
    print("Built list of 10 events: ", events)
    for event in consume_event(events):
        print("Got event from list:", event)
        print("Remains in list:", events)


if __name__ == "__main__":
    main()
