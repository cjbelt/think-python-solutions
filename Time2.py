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
