# def weather_condition(temperature):
#     if temperature > 7:
#         return "Warm"
#     else:
#         return "Cold"
#
#
# user_input = float(input("Enter temperature: "))
# print(weather_condition(user_input))


# user_input = input("Enter your name: ")
# # message = "Hello %s!" % user_input
# message = f"Hello {user_input}!"
# print(message)

user_input1 = input("Enter your first name: ")
user_input2 = input("Enter your surname: ")
when = "today"
# message = "Hello {} {}!".format(user_input1, user_input2)
# message = "Hello %s %s!" % (user_input1, user_input2)
message = f"Hello {user_input1} {user_input2}! What's up {when}"
print(message)
