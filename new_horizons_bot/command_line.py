"""Module that contains command line handlers."""

import argparse
import logging
import sys

from aiogram import Bot, Dispatcher, executor

from new_horizons_bot.help_handler import help_handler


def start_bot() -> None:
    """Handle the new-horizons-bot CLI command."""
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    parser = argparse.ArgumentParser()
    parser.add_argument("token", nargs="?", help="Telegram Bot API Token.")
    args = parser.parse_args()

    if not args.token:
        logging.error("You don't provided a Telegram Bot API token. How you dare!")
        sys.exit(1)

    bot = Bot(args.token)
    dispatcher = Dispatcher(bot)

    dispatcher.register_message_handler(help_handler, commands=["help"])

    executor.start_polling(dispatcher)
    sys.exit(0)
