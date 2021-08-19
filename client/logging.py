from api import history, balance
from config import ASSET, CURRENCY, CRYPTOCURRENCY, START_CRYPTOCURRENCY
from bot.loader import bot
from bot.config import admins


# Отправка логов
def message(text):
    print(text)
    bot.send_messange(admins, text)


# Лог о покупке
def buy_message_success():
    # Получаем последнюю сделку
    data = history(ASSET)[-1]
    # Отправляем сообщения
    message('Покупка')
    message('Информация о сделке \n\nРынок: ' + data['symbol'] + '\nПокупка: ' + data[
        'commissionAsset'] + '\nКупленный актив: ' + data['qty'] + ' ' + data[
                'commissionAsset'] + '\nПроданный актив: ' + data[
                'quoteQty'] + ' ' + CURRENCY + '\nЦена на момент покупки: ' + data[
                'price'] + ' ' + CURRENCY + '\nКомиссия: ' + data[
                'commission'] + ' ' + CURRENCY + '\nВремя сделки: ' + str(data['time']))
    message('Информация о балансе \n\nБаланс ' + CURRENCY + ': ' + str(
        balance(CURRENCY)['free']) + '\nБаланс ' + CRYPTOCURRENCY + ': ' + str(balance(CRYPTOCURRENCY)['free']))
    message('Прибыль \n\nПрибыль ' + CRYPTOCURRENCY + ': ' + str(
        float(balance(CRYPTOCURRENCY)['free']) - START_CRYPTOCURRENCY))


# Лог о продаже
def sell_message_success():
    # Получаем последнюю сделку
    data = history(ASSET)[-1]
    # Отправляем сообщения
    message('Продажа')
    message('Информация о сделке \n\nРынок: ' + data['symbol'] + '\nПокупка: ' + data[
        'commissionAsset'] + '\nКупленный актив: ' + data['quoteQty'] + ' ' + data[
                'commissionAsset'] + '\nПроданный актив: ' + data[
                'qty'] + ' ' + CRYPTOCURRENCY + '\nЦена на момент продажи: ' + data[
                'price'] + ' ' + CRYPTOCURRENCY + '\nКомиссия: ' + data[
                'commission'] + ' ' + CRYPTOCURRENCY + '\nВремя сделки: ' + str(data['time']))
    message('Информация о балансе \n\nБаланс ' + CURRENCY + ': ' + str(
        balance(CURRENCY)['free']) + '\nБаланс ' + CRYPTOCURRENCY + ': ' + str(balance(CRYPTOCURRENCY)['free']))
    message('Прибыль\n\nПрибыль ' + CRYPTOCURRENCY + ': ' + str(
        float(balance(CRYPTOCURRENCY)['free']) - START_CRYPTOCURRENCY))
