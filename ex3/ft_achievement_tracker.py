import random


class Player:
    def __init__(self, name: str, achv: set = set()):
        self.name = name
        self.achv = achv


def gen_player_achievements() -> set:
    achievements = ["Crafting Genius", "Strategist", "World Savior",
                    "Speed Runner", "Survivor", "Master Explorer",
                    "Treasure Hunter", "Unstoppable", "First Steps",
                    "Collector Supreme", "Untouchable", "Sharp Mind",
                    "Boss Slayer"]
    num_achv = random.randint(1, len(achievements))
    list_achv = random.sample(achievements, num_achv)
    return set(list_achv)


def main():
    achievements = set(["Crafting Genius", "Strategist", "World Savior",
                        "Speed Runner", "Survivor", "Master Explorer",
                        "Treasure Hunter", "Unstoppable", "First Steps",
                        "Collector Supreme", "Untouchable", "Sharp Mind",
                        "Boss Slayer"])
    print("=== Achievement Tracker System ===")
    print()
    alice = Player("Alice")
    bob = Player("Bob")
    charlie = Player("Charlie")
    dylan = Player("Dylan")
    alice.achv = gen_player_achievements()
    bob.achv = gen_player_achievements()
    charlie.achv = gen_player_achievements()
    dylan.achv = gen_player_achievements()
    print("Player Alice: ", alice.achv)
    print("Player Charlie: ", charlie.achv)
    print("Player Bob: ", bob.achv)
    print("Player Dylan: ", dylan.achv)
    print()
    print("All distinct achievments: ",
          bob.achv.union(alice.achv,
                         charlie.achv,
                         dylan.achv
                         ))
    print()
    print("Common achievements: ", alice.achv.intersection(
        bob.achv, alice.achv, dylan.achv
    ))

    print("Only Alice has : ", alice.achv - bob.achv - charlie.achv
          - dylan.achv)
    print("Only Bob has : ", bob.achv - alice.achv - charlie.achv
          - dylan.achv)
    print("Only Charlie has : ", charlie.achv - alice.achv - bob.achv
          - dylan.achv)
    print("Only Dylan has : ", dylan.achv - alice.achv - bob.achv
          - charlie.achv)
    print()
    print("Alice is missing:", achievements - alice.achv)
    print("Bob is missing:", achievements - bob.achv)
    print("Charlie is missing:", achievements - charlie.achv)
    print("Dylan is missing:", achievements - dylan.achv)


if __name__ == "__main__":
    main()
