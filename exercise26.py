def tempguage(temp):
    if temp > 25:
        return "Hot"
    elif temp > 14:
        return "Warm"
    else:
        return "Cold"


print(tempguage(10))
print(tempguage(15))
print(tempguage(16))
print(tempguage(25))
print(tempguage(26))

