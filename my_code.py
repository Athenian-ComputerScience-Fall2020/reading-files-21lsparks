# Collaborators (including web sites where you got help: (enter none if you didn't need help)
# claryse adams

def avg_temp(user_list):
    total = 0
    for x in range(1, len(user_list)):
        total += user_list[x]
    average = total/(len(user_list)-1)
    average = round(average, 2)
    return average


if __name__ == '__main__':
    with open("temps.txt") as file_object:
        contents = file_object.readlines()

    int()
    list_length = len(contents)
    for i in range(1, list_length):
        contents[i] = contents[i].rstrip()
        contents[i] = int(contents[i])
    print(contents)

    print(avg_temp(contents))