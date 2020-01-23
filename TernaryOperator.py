#[on_true] if [expression] else [on_false]

# Program to demonstrate conditional operator
a, b = 10, 20

# Copy value of a in min if a < b else copy b
max = a if a > b else b

print(max)
