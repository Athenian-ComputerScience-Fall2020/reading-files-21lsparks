# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  

def avg_temp():
with open('tempts.txt') as file_object:
    contents = file_object.readlines()

list_length = len(avg_temp)
for i in range(avg_temp):
    avg_temp[i] = avg_temp[i].rstrip()
print(avg_temp)

    return


if __name__ == '__main__':
    print(avg_temp())

