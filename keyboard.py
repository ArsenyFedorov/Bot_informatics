from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from text import *


class SimpleCallback(CallbackData, prefix="scb"):
    callback: str = " "
    answer: bool = False


def kb_test():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=test_button, callback_data="test")
    keyboard.adjust(1)
    return keyboard.as_markup()


def kb_task_1():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="3", callback_data=SimpleCallback(callback="task_1", answer=False))
    keyboard.button(text="4", callback_data=SimpleCallback(callback="task_1", answer=True))
    keyboard.button(text="5", callback_data=SimpleCallback(callback="task_1", answer=False))
    keyboard.button(text="22", callback_data=SimpleCallback(callback="task_1", answer=False))
    keyboard.adjust(2)
    return keyboard.as_markup()


def kb_task_2():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Африка", callback_data=SimpleCallback(callback="task_2", answer=False))
    keyboard.button(text="Евразия", callback_data=SimpleCallback(callback="task_2", answer=True))
    keyboard.button(text="Южная Америка", callback_data=SimpleCallback(callback="task_2", answer=False))
    keyboard.button(text="Австралия", callback_data=SimpleCallback(callback="task_2", answer=False))
    keyboard.adjust(2)
    return keyboard.as_markup()


def kb_task_3():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="23", callback_data=SimpleCallback(callback="task_3", answer=False))
    keyboard.button(text="34", callback_data=SimpleCallback(callback="task_3", answer=False))
    keyboard.button(text="45", callback_data=SimpleCallback(callback="task_3", answer=False))
    keyboard.button(text="46", callback_data=SimpleCallback(callback="task_3", answer=True))
    keyboard.adjust(2)
    return keyboard.as_markup()


def kb_task_4():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="8", callback_data=SimpleCallback(callback="task_4", answer=False))
    keyboard.button(text="9", callback_data=SimpleCallback(callback="task_4", answer=False))
    keyboard.button(text="16", callback_data=SimpleCallback(callback="task_4", answer=False))
    keyboard.button(text="7", callback_data=SimpleCallback(callback="task_4", answer=True))
    keyboard.adjust(2)
    return keyboard.as_markup()


def kb_task_5():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="3", callback_data=SimpleCallback(callback="task_5", answer=True))
    keyboard.button(text="2.5", callback_data=SimpleCallback(callback="task_5", answer=False))
    keyboard.button(text="5", callback_data=SimpleCallback(callback="task_5", answer=False))
    keyboard.button(text="81", callback_data=SimpleCallback(callback="task_5", answer=False))
    keyboard.adjust(2)
    return keyboard.as_markup()


def kb_task_6():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Достоевский", callback_data=SimpleCallback(callback="task_6", answer=False))
    keyboard.button(text="Лермонтов", callback_data=SimpleCallback(callback="task_6", answer=False))
    keyboard.button(text="Пушкин", callback_data=SimpleCallback(callback="task_6", answer=True))
    keyboard.button(text="Гоголь", callback_data=SimpleCallback(callback="task_6", answer=False))
    keyboard.adjust(2)
    return keyboard.as_markup()


def kb_task_7():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="4", callback_data=SimpleCallback(callback="task_7", answer=False))
    keyboard.button(text="1", callback_data=SimpleCallback(callback="task_7", answer=False))
    keyboard.button(text="88", callback_data=SimpleCallback(callback="task_7", answer=False))
    keyboard.button(text="64", callback_data=SimpleCallback(callback="task_7", answer=True))
    keyboard.adjust(2)
    return keyboard.as_markup()


def kb_task_8():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="45", callback_data=SimpleCallback(callback="task_8", answer=False))
    keyboard.button(text="90", callback_data=SimpleCallback(callback="task_8", answer=True))
    keyboard.button(text="180", callback_data=SimpleCallback(callback="task_8", answer=False))
    keyboard.button(text="0", callback_data=SimpleCallback(callback="task_8", answer=False))
    keyboard.adjust(2)
    return keyboard.as_markup()


def kb_task_9():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Челябинск", callback_data=SimpleCallback(callback="task_9", answer=False))
    keyboard.button(text="Москва", callback_data=SimpleCallback(callback="task_9", answer=True))
    keyboard.button(text="Санкт-Петербург", callback_data=SimpleCallback(callback="task_9", answer=False))
    keyboard.button(text="Киев", callback_data=SimpleCallback(callback="task_9", answer=False))
    keyboard.adjust(2)
    return keyboard.as_markup()


def kb_task_10():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="HO", callback_data=SimpleCallback(callback="task_10", answer=False))
    keyboard.button(text="OH2", callback_data=SimpleCallback(callback="task_10", answer=False))
    keyboard.button(text="CuO", callback_data=SimpleCallback(callback="task_10", answer=False))
    keyboard.button(text="H2O", callback_data=SimpleCallback(callback="task_10", answer=True))
    keyboard.adjust(2)
    return keyboard.as_markup()



