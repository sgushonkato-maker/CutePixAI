from aiogram.fsm.state import StatesGroup, State


class ArtState(StatesGroup):

    waiting_photo = State()

    waiting_style = State()

    generating = State()