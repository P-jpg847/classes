from datetime import date

class LotteryDraw:
    def __init__(self, round_week: int, round_date: date, numbers: list):
        self.round_week = round_week
        self.round_date = round_date
        self.numbers = numbers

#create a new lotterydraw object
round_1 = LotteryDraw(1, date(2026, 10, 5), [1, 2, 3, 4, 5])

print(round_1.round_week)
print(round_1.round_date)

for number in round_1.numbers:
    print(number)


class Book:
    def __init__(self, title: str, author: str, year: int, genre: str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

bookie = Book("The Subtle Art of Not Giving a F*ck", "Mark Manson", 2016, "Self-Help")

print(bookie.title)