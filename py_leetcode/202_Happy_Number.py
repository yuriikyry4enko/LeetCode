class Solution:
    def isHappy(self, n: int) -> bool:

        failed_set = set()
        while n not in failed_set:
            if n == 1:
                return True
            failed_set.add(n)
            n = self.transform(n)
        return False

    def transform(self, n):
        sumNumbers = 0
        for num in str(n):
            sumNumbers += int(num) ** 2
        return sumNumbers