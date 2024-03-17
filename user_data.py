from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import Router

fsm_router = Router()


class UserData(StatesGroup):
    tg_id = State()
    surname = State()
    name = State()
    class_number = State()
    points = State()
