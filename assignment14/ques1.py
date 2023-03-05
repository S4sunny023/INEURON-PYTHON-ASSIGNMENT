'''Question 1:
Define a class with a generator which can iterate the numbers, which are divisible by
7, between a given range 0 and n.'''

class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def divisible_by_seven(self):
        for i in range(self.n):
            if i % 7 == 0:
                yield i

no= int(input("Enter the range of no:"))

divisible_by_seven_obj = DivisibleBySeven(no)

for num in divisible_by_seven_obj.divisible_by_seven():
    print(num)