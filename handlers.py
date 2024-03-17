from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from keyboard import *
from data_base.user import User
from data_base.result_test import ResultTest
from user_data import fsm_router, UserData
import sqlite3

handlers_router = Router()


@handlers_router.message(Command("start"))
async def start(message: Message, bot: Bot, state: FSMContext):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    user = User(message.from_user.id)
    result_test = ResultTest(message)
    if user.tg_id != 1:
        await bot.send_photo(chat_id=message.from_user.id, caption=user_return,
                             photo="https://kartinki.pics/uploads/posts/2022-03/"
                                   "thumbs/1647966213_"
                                   "3-kartinkin-net-p-kartinki-dlya-prezi-3.jpg",
                             reply_markup=kb_test())
    else:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo="https://avatars.mds.yandex.net/i?id=2a594052b2a26bc287ee5054ef03b55543cda86e"
                                   "-8995617-images-thumbs&n=13", caption=greeting)
        await state.set_state(UserData.surname)
        await bot.send_message(chat_id=message.from_user.id, text=user_surname)


@fsm_router.message(UserData.surname)
async def input_surname(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(surname=message.text)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 2)

    await bot.send_message(chat_id=message.chat.id, text=user_name)
    await state.set_state(UserData.name)


@fsm_router.message(UserData.name)
async def input_name(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(name=message.text)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
    await bot.send_message(chat_id=message.chat.id, text=user_class_number)
    await state.set_state(UserData.class_number)


@fsm_router.message(UserData.class_number)
async def input_class_number(message: Message, state: FSMContext, bot: Bot):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    if len(message.text) < 2 or len(message.text) > 2:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        await bot.send_message(chat_id=message.chat.id, text=error_class_number)
    else:
        await state.update_data(class_number=message.text)
        await state.update_data(tg_id=message.from_user.id)
        our_data = await state.get_data()
        user = User(our_data)
        await state.clear()
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        await bot.send_message(chat_id=message.from_user.id, text=luck, reply_markup=kb_test())


@handlers_router.callback_query(F.data == "test")
async def com_start(callback: CallbackQuery, bot: Bot):
    await bot.send_message(text=task_1, chat_id=callback.message.chat.id, reply_markup=kb_task_1())
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)


@handlers_router.callback_query(SimpleCallback.filter(F.callback == "task_1"))
async def day_class(callback: CallbackQuery, bot: Bot, callback_data: SimpleCallback):
    result_test = ResultTest(callback.from_user.id)
    if callback_data.answer:
        result_test.task_1 = 1
        result_test.save()
    else:
        result_test.task_1 = 0
        result_test.save()
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_message(chat_id=callback.message.chat.id, text=task_2, reply_markup=kb_task_2())


@handlers_router.callback_query(SimpleCallback.filter(F.callback == "task_2"))
async def day_class(callback: CallbackQuery, bot: Bot, callback_data: SimpleCallback):
    result_test = ResultTest(callback.from_user.id)
    if callback_data.answer:
        result_test.task_2 = 1
        result_test.save()
    else:
        result_test.task_2 = 0
        result_test.save()
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_message(chat_id=callback.message.chat.id, text=task_3, reply_markup=kb_task_3())


@handlers_router.callback_query(SimpleCallback.filter(F.callback == "task_3"))
async def day_class(callback: CallbackQuery, bot: Bot, callback_data: SimpleCallback):
    result_test = ResultTest(callback.from_user.id)
    if callback_data.answer:
        result_test.task_3 = 1
        result_test.save()
    else:
        result_test.task_3 = 0
        result_test.save()
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_message(chat_id=callback.message.chat.id, text=task_4, reply_markup=kb_task_4())


@handlers_router.callback_query(SimpleCallback.filter(F.callback == "task_4"))
async def day_class(callback: CallbackQuery, bot: Bot, callback_data: SimpleCallback):
    result_test = ResultTest(callback.from_user.id)
    if callback_data.answer:
        result_test.task_4 = 1
        result_test.save()
    else:
        result_test.task_4 = 0
        result_test.save()
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_message(chat_id=callback.message.chat.id, text=task_5, reply_markup=kb_task_5())


@handlers_router.callback_query(SimpleCallback.filter(F.callback == "task_5"))
async def day_class(callback: CallbackQuery, bot: Bot, callback_data: SimpleCallback):
    result_test = ResultTest(callback.from_user.id)
    if callback_data.answer:
        result_test.task_5 = 1
        result_test.save()
    else:
        result_test.task_5 = 0
        result_test.save()
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_message(chat_id=callback.message.chat.id, text=task_6, reply_markup=kb_task_6())


@handlers_router.callback_query(SimpleCallback.filter(F.callback == "task_6"))
async def day_class(callback: CallbackQuery, bot: Bot, callback_data: SimpleCallback):
    result_test = ResultTest(callback.from_user.id)
    if callback_data.answer:
        result_test.task_6 = 1
        result_test.save()
    else:
        result_test.task_6 = 0
        result_test.save()
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_message(chat_id=callback.message.chat.id, text=task_7, reply_markup=kb_task_7())


@handlers_router.callback_query(SimpleCallback.filter(F.callback == "task_7"))
async def day_class(callback: CallbackQuery, bot: Bot, callback_data: SimpleCallback):
    result_test = ResultTest(callback.from_user.id)
    if callback_data.answer:
        result_test.task_7 = 1
        result_test.save()
    else:
        result_test.task_7 = 0
        result_test.save()
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_message(chat_id=callback.message.chat.id, text=task_8, reply_markup=kb_task_8())


@handlers_router.callback_query(SimpleCallback.filter(F.callback == "task_8"))
async def day_class(callback: CallbackQuery, bot: Bot, callback_data: SimpleCallback):
    result_test = ResultTest(callback.from_user.id)
    if callback_data.answer:
        result_test.task_8 = 1
        result_test.save()
    else:
        result_test.task_8 = 0
        result_test.save()
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_message(chat_id=callback.message.chat.id, text=task_9, reply_markup=kb_task_9())


@handlers_router.callback_query(SimpleCallback.filter(F.callback == "task_9"))
async def day_class(callback: CallbackQuery, bot: Bot, callback_data: SimpleCallback):
    result_test = ResultTest(callback.from_user.id)
    if callback_data.answer:
        result_test.task_9 = 1
        result_test.save()
    else:
        result_test.task_9 = 0
        result_test.save()
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_message(chat_id=callback.message.chat.id, text=task_10, reply_markup=kb_task_10())


@handlers_router.callback_query(SimpleCallback.filter(F.callback == "task_10"))
async def day_class(callback: CallbackQuery, bot: Bot, callback_data: SimpleCallback):
    result_test = ResultTest(callback.from_user.id)
    if callback_data.answer:
        result_test.task_10 = 1
        result_test.save()
    else:
        result_test.task_10 = 0
        result_test.save()
    result_test.total = 0
    result_test.total += result_test.task_1 + result_test.task_2 + result_test.task_3 + result_test.task_4 + result_test.task_5 + result_test.task_6 + result_test.task_7 + result_test.task_8 + result_test.task_9 + result_test.task_10
    result_test.save()
    user = User(callback.from_user.id)
    user.points = result_test.total
    user.save()
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.send_message(chat_id=callback.message.chat.id, text=complete + str(result_test.total))
