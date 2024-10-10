from fake_math import divide as fake_divide
from true_math import divide as true_divide

result1 = fake_divide(39, 3)
result2 = fake_divide(9, 0)
result3 = true_divide(64, 8)
result4 = true_divide(120, 0)

print(result1)
print(result2)
print(result3)
print(result4)