from stack import Stack

default_string = "nam a ma I"

reverse_string = ""

s = Stack()
for char in default_string:
    if char != " ":
        s.push(char)

while not s.is_empty():
    reverse_string += s.pop()

print(reverse_string)



