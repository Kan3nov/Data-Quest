import random


def main():
    names = ["Alice", "bob", "Charlie", "dylan",
             "Emma", "Gregory", "john", "kevin", "Liam"]
    print("Initial list of players:", names)
    list_cap_all = [name.capitalize() for name in names]
    print("New list with all names capitalized:", list_cap_all)
    list_cap_only = [name for name in names if name[0].isupper()]
    print("New list of capitalized names only:", list_cap_only)
    print()
    dict_rand_scores = {name: random.randint(1, 1000) for name
                        in list_cap_all}
    print("Score dict:", dict_rand_scores)

    total_score = 0
    for name in list_cap_all:
        total_score += dict_rand_scores[name]
    average = total_score / len(dict_rand_scores)
    dict_avg_scores = {name: dict_rand_scores[name] for name
                       in list_cap_all if dict_rand_scores[name] > average}
    print("Score average is", round(average, 1))
    print("High scores:", dict_avg_scores)


if __name__ == "__main__":
    main()
