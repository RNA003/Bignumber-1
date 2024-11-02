class BigNumber:
    def __init__(self, num_str):
        self.digits = [int(digit) for digit in reversed(num_str)]

    def __str__(self):
        return ''.join(map(str, reversed(self.digits)))

    def add(self, other):
        result = []
        carry = 0
        i, j = len(self.digits) - 1, len(other.digits) - 1
        while i >= 0 or j >= 0 or carry:
            digit_sum = carry
            if i >= 0:
                digit_sum += self.digits[i]
            if j >= 0:
                digit_sum += other.digits[j]
            result.append(digit_sum % 10)
            carry = digit_sum // 10
            i -= 1
            j -= 1
        result.reverse()
        return BigNumber(''.join(map(str, result)))

    def subtract(self, other):
        result = []
        borrow = 0
        i, j = len(self.digits) - 1, len(other.digits) - 1
        while i >= 0 or j >= 0:
            diff = borrow
            if i >= 0:
                diff += self.digits[i]
            if j >= 0:
                diff -= other.digits[j]
            result.append((diff + 10) % 10)
            borrow = -1 if diff < 0 else 0
            i -= 1
            j -= 1
        while result and result[-1] == 0:
            result.pop()
        if borrow:
            result.insert(0, -1)
        result.reverse()
        return BigNumber(''.join(map(str, result)))

    def multiply(self, other):
        result = [0] * (len(self.digits) + len(other.digits))
        for i in range(len(self.digits)):
            carry = 0
            for j in range(len(other.digits)):
                product = self.digits[i] * other.digits[j] + carry
                result[i + j] += product % 10
                carry = product // 10
            result[i + j + 1] += carry
        while result and result[-1] == 0:
            result.pop()
        result.reverse()
        return BigNumber(''.join(map(str, result)))

    def power(self, n):

        if n == 0:
            return BigNumber('1')
        elif n == 1:
            return self
        elif n % 2 == 0:
            temp = self.power(n // 2)
            return temp.multiply(temp)
        else:
            temp = self.power(n // 2)
            return temp.multiply(temp).multiply(self)

        def shift_left(self, n):

            result = [0] * n + self.digits
            return BigNumber(''.join(map(str, result)))

        def shift_right(self, n):

            return BigNumber(''.join(map(str, self.digits[n:])))