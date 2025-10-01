# Classes used to find the average values of the
# random numbers over a specified time period


from datetime import datetime, timedelta


class OneMinute:

    def __init__(self):
        self.num = []
        self.next_period = datetime.now() + timedelta(minutes=1)

    def add_value(self, num):
        self.num.append(num)
        return self.num

    def get_average(self):
        return sum(self.num) / len(self.num)

    def check_time(self):
        return self.next_period

    def reset(self):
        self.num = []
        self.next_period = datetime.now() + timedelta(minutes=1)


class FiveMinute:

    def __init__(self):
        self.num = []
        self.next_period = datetime.now() + timedelta(minutes=5)

    def add_value(self, num):
        self.num.append(num)
        return self.num

    def get_average(self):
        return sum(self.num) / len(self.num)

    def check_time(self):
        return self.next_period

    def reset(self):
        self.num = []
        self.next_period = datetime.now() + timedelta(minutes=5)


class ThirtyMinute:

    def __init__(self):
        self.num = []
        self.next_period = datetime.now() + timedelta(minutes=30)

    def add_value(self, num):
        self.num.append(num)
        return self.num

    def get_average(self):
        return sum(self.num) / len(self.num)

    def check_time(self):
        return self.next_period

    def reset(self):
        self.num = []
        self.next_period = datetime.now() + timedelta(minutes=30)

