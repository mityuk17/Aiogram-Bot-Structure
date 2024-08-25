from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from database.crud.user import get_user, create_user
import texts.general as general_texts


router = Router(name="General")


@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer(text=general_texts.start())
    
    await state.update_data({"last_action": "start-command"})