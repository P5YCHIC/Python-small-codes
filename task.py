import array
arr = []
_ = True
while _:
    arr_num = int(input("Enter number:"))
    arr.append(arr_num)
    ask_user = input("Is there more number?Type 'y' for yes and 'n' for no.").lower()
    if ask_user == 'y':
        _ = True
    elif ask_user =='n':
        _ = False







