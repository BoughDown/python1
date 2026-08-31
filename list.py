"""
Lecture on lists/for loops
"""

test_list = []

for i in range(5):
    print(f"hello number {i}")
    test_list.append(i+1)

    print(test_list)

test_list.append(2)
print(test_list)
test_list2 = test_list + ["a", "b"]
print(test_list2)
# print(test_list.count(2))