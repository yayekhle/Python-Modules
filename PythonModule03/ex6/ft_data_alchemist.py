# ft_data_alchemist.py
import random


def main():
    print("=== Game Data Alchemist ===")

    players = [
        "Alice", "bob", "Charlie", "dylan", "Emma", "Gregory",
        "john", "kevin", "Liam"]

    print("Initial list of players:", players)

    all_capitalized = []
    for name in players:
        capitalized_name = name.capitalize()
        all_capitalized.append(capitalized_name)

    already_capitalized = []
    for name in players:
        if name[0].isupper():
            already_capitalized.append(name)
    print("New list with all names capitalized:", all_capitalized)
    print("New list of capitalized names only:", already_capitalized)

    scores = {}
    for name in all_capitalized:
        score = random.randint(50, 1000)
        scores[name] = score

    print("Score dict:", scores)

    avg_score = sum(scores.values()) / len(scores)
    print(f"Score average is {avg_score:.2f}")

    high_scores = {}
    for name, score in scores.items():
        if score > avg_score:
            high_scores[name] = score
    print("High scores:", high_scores)


if __name__ == "__main__":
    main()
