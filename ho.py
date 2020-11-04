
def avg(user_list):
    # Insert code here
    average = sum(user_list)/len(user_list)
    return average


if __name__ == '__main__':
    num_list = []
    print("Input a number to be averaged. When finished with numbers, type 'done'")
    while True:
        tba = (input("Number: "))
        if tba.isnumeric():
            num_list.append(int(tba))
        elif tba == "done":
            break
        else:
            print("That's Invalid. Try again.")
    print(avg(num_list))
