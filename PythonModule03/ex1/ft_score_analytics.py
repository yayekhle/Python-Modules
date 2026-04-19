import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    scores = []

    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if not scores:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              "<score1> <score2> ...")
    else:
        print("Scores processed:", scores)
        print("Total players:", len(scores))
        print("Total score:", sum(scores))
        avg = sum(scores) / len(scores)
        print("Average score:", avg)
        print("High score:", max(scores))
        print("Low score:", min(scores))
        print("Score range:", max(scores) - min(scores))


if __name__ == "__main__":
    main()
