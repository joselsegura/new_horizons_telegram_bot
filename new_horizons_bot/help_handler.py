from aiogram import types


async def help_handler(msg: types.Message) -> None:
    """"Handle help message from an user"""
    help_text = "This is a help text for testing"
    await msg.answer(help_text)
    await msg.reply("Son of a bitch, hay que decirlo mas")
