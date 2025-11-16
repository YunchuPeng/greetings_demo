from argparse import ArgumentParser
from art import art
from .greeter import greet


def process():
    """Parse command-line arguments and print the greeting."""
    parser = ArgumentParser(description="Generate appropriate greetings")

    # 可选参数：称呼
    parser.add_argument("--title", "-t", help="Optional title, e.g. Dr, Prof")

    # 可选参数：礼貌模式，只写了就会是 True
    parser.add_argument(
        "--polite",
        "-p",
        action="store_true",
        help="Use a formal greeting instead of casual",
    )

    # 位置参数：名字和姓氏（必填）
    parser.add_argument("personal", help="Given name")
    parser.add_argument("family", help="Family name")

    args = parser.parse_args()

    message = greet(args.personal, args.family, args.title, args.polite)
    print(art("cute face"), message)


if __name__ == "__main__":
    process()
