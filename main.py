n = int(input("Nechta son kiritasiz: "))

max_son = int(input("1-sonni kiriting: "))

for i in range(2, n + 1):
    son = int(input(f"{i}-sonni kiriting: "))
    if son > max_son:
        max_son = son

print("Eng katta son:", max_son)
