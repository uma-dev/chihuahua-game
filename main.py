import argparse
from gym_ext.train import train, evaluate


def main():
    parser = argparse.ArgumentParser(description="Train or evaluate Chihuahua RL agent")
    parser.add_argument(
        "mode", choices=["train", "eval"], help="Run training or evaluation"
    )
    args = parser.parse_args()

    if args.mode == "train":
        train()
    elif args.mode == "eval":
        evaluate()


if __name__ == "__main__":
    main()
