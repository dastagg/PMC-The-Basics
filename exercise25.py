def checkpass(password):
    if len(password) < 8:
        return False
    else:
        return True


print(checkpass("mypass"))
print(checkpass("mylongpassword"))
