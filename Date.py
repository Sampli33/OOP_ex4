class Date:
    """
    Represents a date in the format 'dd.mm.yyyy'.

    Attributes:
        formatted_months (list): A list of abbreviated month names in Russian.
        thirty_one (list): A list of months with 31 days.
        thirty (list): A list of months with 30 days.
        day_months (list): A list of days in each month.
    """

    formatted_months = ['янв', 'фев', 'мар', 'апр',
                        'май', 'июн', 'июл', 'авг',
                        'сен', 'окт', 'ноя', 'дек']
    thirty_one = [1, 3, 5, 7, 8, 10, 12]
    thirty = [4, 6, 9, 11]
    day_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, date):
        """
        Initializes a Date object with the provided date string in 'dd.mm.yyyy' format.

        Args:
            date (str): A string representing the date in 'dd.mm.yyyy' format.
        """
        try:
            day, month, year = map(str, date.split('.'))
            if len(day) != 2 or len(month) != 2:
                raise ValueError
            day, month, year = int(day), int(month), int(year)
            if not (1 <= month <= 12 and 1970 <= year <= 2024):
                raise ValueError
            if month in Date.thirty_one and not (1 <= day <= 31):
                raise ValueError
            if month in Date.thirty and not (1 <= day <= 30):
                raise ValueError
            if month == 2 and not (1 <= day <= 29):
                raise ValueError
            if month == 2 and not ((year % 4 == 0 and year % 100 != 0)
                                   or year % 400 == 0) and not (1 <= day <= 28):
                raise ValueError
            self.__date = date

        except (ValueError, AttributeError):
            self.__date = None
            print('ошибка')

    @property
    def date(self):
        """
        Gets the formatted date string.

        Returns:
            str: The formatted date string.
        """
        if self.__date:
            day, month, year = map(int, self.__date.split('.'))
            return f'{day} {Date.formatted_months[month - 1]} {year} г.'
        else:
            return None

    @date.setter
    def date(self, date):
        """
        Sets the date.

        Args:
            date (str): A string representing the date in 'dd.mm.yyyy' format.
        """
        try:
            day, month, year = map(str, date.split('.'))
            if len(day) != 2 or len(month) != 2:
                raise ValueError
            day, month, year = int(day), int(month), int(year)
            if not (1 <= month <= 12 and 1970 <= year <= 2024):
                raise ValueError
            if month in Date.thirty_one and not (1 <= day <= 31):
                raise ValueError
            if month in Date.thirty and not (1 <= day <= 30):
                raise ValueError
            if month == 2 and not (1 <= day <= 29):
                raise ValueError
            if month == 2 and not ((year % 4 == 0 and year % 100 != 0)
                                   or year % 400 == 0) and not (1 <= day <= 28):
                raise ValueError
            self.__date = date

        except (ValueError, AttributeError):
            self.__date = None
            print('ошибка')

    def to_timestamp(self):
        """
        Converts the date to a Unix timestamp.

        Returns:
            int: The Unix timestamp representing the date.
        """
        if self.__date:
            day, month, year = map(int, self.__date.split('.'))
            years = year - 1970
            months_days = sum(Date.day_months[:month - 1])
            leap_year = years // 4 - years // 100 + years // 400
            days = (day - 1) + leap_year
            if month > 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
                days += 1
            seconds = (years * 365 + months_days + days) * 24 * 60 * 60
            return seconds
        else:
            return None

    def __lt__(self, other):
        """
        Checks if this date is less than another date.
        """
        return self.to_timestamp() < other.to_timestamp()

    def __le__(self, other):
        """
        Checks if this date is less than or equal to another date.
        """
        return self.to_timestamp() <= other.to_timestamp()

    def __eq__(self, other):
        """
        Checks if this date is equal to another date.
        """
        return self.to_timestamp() == other.to_timestamp()

    def __ne__(self, other):
        """
        Checks if this date is not equal to another date.
        """
        return self.to_timestamp() != other.to_timestamp()

    def __gt__(self, other):
        """
        Checks if this date is greater than another date.
        """
        return self.to_timestamp() > other.to_timestamp()

    def __ge__(self, other):
        """
        Checks if this date is greater than or equal to another date.
        """
        return self.to_timestamp() >= other.to_timestamp()

    def __str__(self):
        """
        Returns a string representation of the date.
        """
        if self.__date:
            return self.__date
        else:
            return 'None'
