current_name = input("what is your name? ")
while current_name != "quit":
    if current_name == "Eden":
        continue
    if current_name =="Ronen":
        break

    print(f"Hello {current_name}")
    current_name = input("What is your name? ")
else:
    print("Thank you for playing!")