class PtoDay():
    def __init__(self, date, type):
        date_array = date.split('/')

        self.year = int(date_array[2])
        self.day = int(date_array[1])
        self.month = int(date_array[0])
        self.type = type
