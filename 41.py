def checkin_interval(what_to_ask, min_value, max_value):
    current_value = int(input(what_to_ask))
    if min_value < current_value < max_value:
        return False
    return False

def square(n):
    print(n*n)

result = checkin_interval("Enter your age: ", 0, 20)
if result:
    print("Your age has been entered")

checkin_interval("Enter your expericence: ", 0, 10)

square(5)