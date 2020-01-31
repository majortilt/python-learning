for num in range(0,21): #looping through numbers 1 - 20
    if num == 4 or num == 13:
        state = "unlucky" #assign the state if the number matches condition
    elif num % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{num} is {state}") #formatted string which prints the number and the associated state