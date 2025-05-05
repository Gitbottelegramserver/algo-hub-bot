from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command
from app.keyboards.keyboards import main_menu_kb, modules_menu_kb
from app.modules.module_descriptions import get_description
from app.dialogs.dialogs import WELCOME_TEXT, PAYMENT_TEXT, SUPPORT_TEXT

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(WELCOME_TEXT, reply_markup=main_menu_kb)

@router.callback_query(F.data == "show_modules")
async def show_modules_handler(callback: CallbackQuery):
    await callback.message.edit_text("📚 Выберите модуль обучения:", reply_markup=modules_menu_kb)
    await callback.answer()

@router.callback_query(F.data == "payment")
async def payment_handler(callback: CallbackQuery):
    await callback.message.answer(PAYMENT_TEXT)
    await callback.answer()

@router.callback_query(F.data == "support")
async def support_handler(callback: CallbackQuery):
    await callback.message.answer(SUPPORT_TEXT)
    await callback.answer()

@router.callback_query(F.data.startswith("module_"))
async def module_description_handler(callback: CallbackQuery):
    module_number = int(callback.data.split("_")[1])
    text = get_description(module_number)
    await callback.message.answer(text)
    await callback.answer()
