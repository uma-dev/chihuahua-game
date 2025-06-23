import argparse
from gym_ext.train import train, evaluate


def main():
    parser = argparse.ArgumentParser(description="Train or evaluate Chihuahua RL agent")
    parser.add_argument(
        "mode",
        choices=["train_render", "train_no_render", "eval"],
        help="Run training or evaluation",
    )
    args = parser.parse_args()

    if args.mode == "train_render":
        train(render_mode="human")
    elif args.mode == "train_no_render":
        train(render_mode=None)
    elif args.mode == "eval":
        evaluate()


if __name__ == "__main__":
    main()
