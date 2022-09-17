def need_coat(temp):
    if temp > 7:
        return "Warm"
    else:
        return "Cold"


print(need_coat(10))
print(need_coat(7))
print(need_coat(5))
