def reverse_list(lst):
    return lst[::-1]

my_list = [1, 2, 3, 4, 5]
print(reverse_list(my_list))

Q2.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0


stack = Stack()
stack.push(10)
stack.push(20)
print(stack.peek())  
print(stack.pop())   
print(stack.is_empty())  

Q3.
def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n - 1)

# Example:
countdown(5)

Q4. 
def sum_up_to_n(n, total=0):
    if n == 0:
        return total
    return sum_up_to_n(n - 1, total + n)

# Example:
print(sum_up_to_n(5))  # 15

Q5.
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Example:
string = "data structures and algorithms"
print(char_frequency(string))