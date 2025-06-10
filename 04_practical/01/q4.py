def sum_up_to_n(n, total=0):
    if n == 0:
        return total
    return sum_up_to_n(n - 1, total + n)


print(sum_up_to_n(5))  