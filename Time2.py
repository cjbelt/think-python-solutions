from Time1 import int_to_time

class Time(object):
    """Represents the time of day.

    attributes: hour, minute, second.
    """
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.seconds
        return seconds

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def __lt__(self, other):
        seconds = self.time_to_int() - other.time_to_int()
        return seconds < 0

    def __gt__(self, other):
        seconds = self.time_to_int() - other.time_to_int()
        return seconds > 0

    def __eq__(self, other):
        return self.time_to_int() == self.time_to_int()
