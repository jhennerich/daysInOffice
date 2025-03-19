class PtoDay():
    def __init__(self, date, type):
        date_array = date.split('/')

        self.year = int(date_array[2])
        self.day = int(date_array[1])
        self.month = int(date_array[0])
        if type == 'holiday':
            self.type = 'holiday'
        else:
            self.type = 'pto'
