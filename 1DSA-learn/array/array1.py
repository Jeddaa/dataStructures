class MonthlyExpense:
    def __init__(self, nums):
        self.nums = nums

    def compareFebToJan(self):
        return self.nums[1] - self.nums[0]

    def totalFirstQuarter(self):
        total = 0
        for i in range(0, 3):
            total = total + self.nums[i]
        return total

    def exact2000(self):
        # either use for loop (line 16-19) or just use line 20
        # for i in range(0, len(self.nums)):
        #     if self.nums[i] == 2000:
        #           True
        #     return False
        return 2000 in self.nums

    def addJune(self, june):
        self.nums.append(june)
        return self.nums

    def returnApril(self, fee):
        self.nums[3] = 2130-fee
        return self.nums


test = MonthlyExpense([2200, 2350, 2600, 2130, 2190])
print(test.compareFebToJan())
print(test.totalFirstQuarter())
print(test.exact2000())
print(test.addJune(1980))
print(test.returnApril(200))
