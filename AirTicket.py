class AirTicket:

    def __init__(self, info):
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
        output = (f'|{self.passenger_name.ljust(16)}|{self._from.ljust(4)}|'
                  f'{self.to.ljust(3)}|{self.date_time.ljust(16)}|{self.flight.ljust(20)}|'
                  f'{self.seat.ljust(4)}|{self._class.ljust(3)}|{self.gate.ljust(4)}')
        return output


class Load:
    data = []

    @classmethod
    def write(cls, file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            for man in f.readlines()[1:]:
                passenger = AirTicket(man.strip())
                Load.data.append(passenger)
