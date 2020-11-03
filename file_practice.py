# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#


# Read temps.txt and print it without the blank line at the end



# Read temps.txt line by line and print with no whitespace



# Make a list of lines from the file



# Edit the elements to eliminate whitespace in the list


with open('tempts.txt') as file_object:
    contents = file_object.readlines()

list_length = len(line_list)
for i in range(list_length):
    line_list[i] = linelist[i].rstrip()
print(line_list)

