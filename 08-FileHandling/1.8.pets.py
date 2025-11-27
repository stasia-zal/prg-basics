###
# Reads the entire contents of a file
#
def read_from_file(name):
    with open(name) as file:
        content = file.read()
    return content

# reads the entire file and splits lines into array
file_content = read_from_file('pets.txt')
file_lines = file_content.split()

num_words=0
for word in file_lines:
    num_words+=1
print(file_content,'\n','Number of words', num_words)
