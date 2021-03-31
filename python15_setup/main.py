# coding=utf-8
# This is a sample Python script.

# from prettytable import PrettyTable
# x = PrettyTable()
#
# x.field_names = ["pokemon name", "type", "Num"]
# x.add_row(["Pikachu", "Electricity", 25])
# x.add_row(["shui zhan gui", "Electricity", 9])
#
# x.align = "l"
#
#
# print(x)

class Hotel:
    def __init__(self, room_number, days):
        self.room_number = room_number
        self.days = days
    def greeting(self):
        print("May you have good rest in room " + self.room_number + " for "  + self.days + " days." )


P1 = Hotel('3215', '5')
P1.greeting()