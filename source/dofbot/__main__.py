import argparse

from dofbot.dofbot import DofBot


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('token', type=str, help='Telegram API token')

    args = parser.parse_args()

    DofBot(args.token).start()


if __name__ == '__main__':
    main()
