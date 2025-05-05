from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Главное меню
main_menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📚 Курсы по трейдингу", callback_data="show_modules")],
        [InlineKeyboardButton(text="💳 Оплата курса", callback_data="payment")],
        [InlineKeyboardButton(text="⚙️ Настройки и поддержка", callback_data="support")]
    ]
)

# Меню с модулями
modules_menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📘 Модуль 1: Вводный модуль и Безопасность", callback_data="module_1")],
        [InlineKeyboardButton(text="📗 Модуль 2: Арбитраж", callback_data="module_2")],
        [InlineKeyboardButton(text="📙 Модуль 3: Скальп-трейдинг", callback_data="module_3")],
        [InlineKeyboardButton(text="📒 Модуль 4: Smart Money", callback_data="module_4")],
        [InlineKeyboardButton(text="📕 Модуль 5: Волновой анализ", callback_data="module_5")],
        [InlineKeyboardButton(text="📓 Модуль 6: DeFi", callback_data="module_6")],
        [InlineKeyboardButton(text="📔 Модуль 7: Проп трейдинг", callback_data="module_7")]
    ]
)
