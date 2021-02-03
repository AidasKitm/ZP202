# Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
#     If the number is a multiple of 4, print out a different message.
#     Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#     If check divides evenly into num, tell that to the user.
#     If not, print a different appropriate message.
def second_exercise_with_extras():
    user_input = int(input("enter number: "))
    if user_input % 4 == 0:
        print("multiplication out of 4 is possible")
    elif user_input % 2 == 0:
        print("even")
    else:
        print("odd")

def extras2nd_part():
    user_input1 = int(input("first number: "))
    user_input2 = int(input("second number: "))

    if user_input1 % user_input2 == 0:
        print("first number divides evenly from second number")
    else:
        print("doesn't divide evenly")


extras2nd_part()