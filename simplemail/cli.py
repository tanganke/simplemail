import argparse

from .send import send_mail


def main():
    parser = argparse.ArgumentParser(description="Send an email")
    parser.add_argument(
        "--to", type=str, help="email addresses to send the email to", default=None
    )
    parser.add_argument("subject", type=str, help="subject of the email")
    parser.add_argument("contents", type=str, help="contents of the email")

    args = parser.parse_args()

    send_mail(subject=args.subject, contents=args.contents, to=args.to)


if __name__ == "__main__":
    main()
