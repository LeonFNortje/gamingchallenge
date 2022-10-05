import sys

from myapp.app import process_scoresheet, show_results


def main(args):
    if args and args[0]:
        with open(args[0]) as f:
            lines = f.readlines()
    else:
        print(
            "Capture result of game, in format 'team a [score], team b [score]' empty line would return results."
        )
        lines = []
        score = "start"
        while len(score) > 0:
            score = input("Game result: ")
            if len(score) > 0:
                lines.append(score)
    if len(lines) > 0:
        scores = process_scoresheet("\n".join(lines))
        print(show_results(scores))
    else:
        print("No game results found.")
        print("usage: python3 main.py [gameresults.txt]")
    sys.exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])
