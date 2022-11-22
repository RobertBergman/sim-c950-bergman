from datetime import time


class Clock:
    """
    class clock manages the clock for simulation and displays time in military format
    """
    def __init__(self):
        self._current_time = 0
        self._time_events = []
        self._time_hour = 8
        self._time_minute = 0
        self._time_seconds = 0

    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(Clock, cls).__new__(cls)
    #     return cls.instance

    def advance(self):
        """
        O(1) time O(1) Space

        advances the clock 1 second
        :return:
        """
        self._current_time += 1
        self._time_seconds += 1
        if self._time_seconds == 60:
            self._time_seconds = 0
            self._time_minute += 1
            if self._time_minute == 60:
                self._time_minute = 0
                self._time_hour += 1

    @property
    def clock_time(self):
        """
        O(1) Time O(1) Space
        returns the time as a datetime.time object
        :return:
        """
        return time(self._time_hour, self._time_minute, self._time_seconds)

    @property
    def time(self):
        """
        O(1) Time O(1) Space
        returns the time in seconds since 8:00AM
        :return:
        """
        return self._current_time

    def __repr__(self):
        return str(self.clock_time)
