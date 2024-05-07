class AirTicket:
    """
    Represents an air ticket.

    Attributes:
        passenger_name (str): The name of the passenger.
        _from (str): The departure location.
        to (str): The destination location.
        date_time (str): The date and time of the flight.
        flight (str): The flight number.
        seat (str): The seat number.
        _class (str): The class of the ticket.
        gate (str): The gate number.
    """

    def __init__(self, info):
        """
        Initializes an AirTicket object with the provided ticket information.

        Args:
            info (str): A string containing ticket information separated by ';'.
                        The format is 'passenger_name;from;to;date_time;flight;seat;class;gate'.
        """
        pass_info = info.split(';')
        self.passenger_name = pass_info[0]
        self._from = pass_info[1]
        self.to = pass_info[2]
        self.date_time = pass_info[3]
        self.flight = pass_info[4]
        self.seat = pass_info[5]
        self._class = pass_info[6]
        self.gate = pass_info[7]

    def __repr__(self):
        """
        Returns a string representation of the AirTicket object.

        Returns:
            str: A formatted string representing the ticket information.
        """
        output = (f'|{self.passenger_name.ljust(16)}|{self._from.ljust(4)}|'
                  f'{self.to.ljust(3)}|{self.date_time.ljust(16)}|{self.flight.ljust(20)}|'
                  f'{self.seat.ljust(4)}|{self._class.ljust(3)}|{self.gate.ljust(4)}')
        return output


class Load:
    """
    Represents a data loader for air tickets.

    Attributes:
        data (list): A list to store loaded AirTicket objects.
    """
    data = []

    @classmethod
    def write(cls, file_name):
        """
        Reads data from a file and creates AirTicket objects.

        Args:
            file_name (str): The name of the file to read data from.
        """
        with open(file_name, 'r', encoding='utf-8') as f:
            for man in f.readlines()[1:]:
                passenger = AirTicket(man.strip())
                Load.data.append(passenger)
