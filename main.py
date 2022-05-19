import datetime as dt


class Record:
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        self.date = (
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)
    
    def get_today_stats(self):
        today_stats = 0
        """Переменная в цикле называется как класс и с большой буквы (несоблюдение требований к коду)"""
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
        """Не соблюдается консистентность кода (несоблюдение требований к коду)"""
                today_stats = today_stats + Record.amount
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            if (
                (today - record.date).days < 7 and
                (today - record.date).days >= 0
            ):
        """Не соблюдается консистентность кода (несоблюдение требований к коду)"""
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    """Комментарий не по Docstrings и некорректно оформлены (несоблюдение требований к коду)"""
    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        x = self.limit - self.get_today_stats()
        if x > 0:
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        else:
            return('Хватит есть!')


class CashCalculator(Calculator):
    """Комментарии не по Docstrings и некорректно оформлены (несоблюдение требований к коду)"""
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.

    """Метод get_today_cash_remained должен принимать только валюту, курсы валют не должен (несоблюдение требований к заданию)"""
    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        """Ошибка: если курс руб, то осталось денег всегда 1 руб (вместо этого надо было написать  cash_remained /= 1.00) (логическая ошибка / опечатка)"""
        elif currency_type == 'rub':
            cash_remained == 1.00
            currency_type = 'руб'
        if cash_remained > 0:
        """В f-строке указана не переменная с операцией округления;
           не соблюдается консистентность кода: разные способы форматирования строки, 
           разные способы округления (несоблюдение требований к коду)     
        """
            return (
                f'На сегодня осталось {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'Денег нет, держись'
        """Избыточность: вместо elif cash_remained < 0 можно было указать else  (несоблюдение требований к коду)"""
        elif cash_remained < 0:
            return 'Денег нет, держись:' \
                   ' твой долг - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)

    """Непонятно, зачем в классе CashCalculator определять get_week_stats(self),
    отсутствует конструкция if name == '__main__' (несоблюдение требований к коду)
    """
    def get_week_stats(self):
        super().get_week_stats()
