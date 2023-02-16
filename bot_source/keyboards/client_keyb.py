from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

button_flip = KeyboardButton('/Подбросить_монетку')
button_schedule = KeyboardButton('/Узнать_расписание')
button_prediction = KeyboardButton('/Получить_педсказание')

keyboard_start = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_start.add(button_schedule).add(button_flip).add(button_prediction)


button_sept = KeyboardButton('Сентябрь')
button_oct = KeyboardButton('Октябрь')
button_nov = KeyboardButton('Ноябрь')
button_dec = KeyboardButton('Декабрь')
button_jan = KeyboardButton('Январь')
button_feb = KeyboardButton('Февраль')
button_march = KeyboardButton('Март')
button_apr = KeyboardButton('Апрель')
button_may = KeyboardButton('Май')
button_june = KeyboardButton('Июнь')
button_july = KeyboardButton('Июль')
button_aug = KeyboardButton('Август')

keyboard_months = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_months.row(button_sept, button_oct, button_nov, button_dec).row(
    button_jan, button_feb, button_march, button_apr).row(
    button_may, button_june, button_july, button_aug
)
keyboard_remove = ReplyKeyboardRemove()
