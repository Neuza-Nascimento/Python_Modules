#!/usr/bin/python3

import sys


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
    else:
        args = []
        for i in sys.argv[1:]:
            try:
                args.append(int(i))
            except ValueError:
                print(f"Invalid parameter: '{i}'")
        if len(args) == 0:
            print("No scores provided. Usage: python3 "
                  "ft_score_analytics.py <score1> <score2> ...")
        else:
            print("Scores processed: [", end="")
            for arg in args:
                print(f" {arg}", end="")
            print(" ]")
            print(f"Total players: {len(args)}")
            print(f"Total score: {sum(args)}")
            print(f"Average score: {sum(args) / len(args)}")
            print(f"High score: {max(args)}")
            print(f"Low score: {min(args)}")
            print(f"Score range: {max(args) - min(args)}")


def main() -> None:
    ft_score_analytics()


if __name__ == "__main__":
    main()
