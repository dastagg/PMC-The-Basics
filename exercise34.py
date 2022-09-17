
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for key, value in phone_numbers.items():
    new_value = value.replace("+", "00")
    print(f"{new_value}")
