def operate(operator, *nums):
    def addition():
        result = sum(nums)
        return result

    def subtraction():
        result = 0
        for n in nums:
            if n == nums[0]:
                result = n
            else:
                result -= n
        return result

    def multiplication():
        result = 1
        for n in nums:
            result *= n
        return result

    def divison():
        result = 0
        for n in nums:
            if n == nums[0]:
                result = n
            else:
                if result != 0:
                    result /= n

        return result

    if operator == '+':
        return addition()
    elif operator == '-':
        return subtraction()
    elif operator == '*':
        return multiplication()
    elif operator == '/':
        return divison()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("-", 11, 8, 5))
print(operate("/", 6, 2))
