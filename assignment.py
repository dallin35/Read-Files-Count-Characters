# CIS 3330 - CODE 3
# Use file_content variable to conduct your analysis
# Hanh Doan

file_content = open('Office_Products_Modified.txt').read()


def get_number_of_a():
    count = 0
    for letter in file_content:
        if letter.lower() == 'a':
            count = count + 1
    return count

def get_number_of_z():
    count = 0
    for letter in file_content:
        if letter.lower() == 'z':
            count = count + 1
    return count

def get_number_of_percent():
    count = 0
    for letter in file_content:
        if letter == '%':
            count = count + 1
    return count


def get_number_of_char(user_char):
    count = 0
    target = user_char.lower()
    for letter in file_content:
        if letter.lower() == target:
            count = count + 1
    return count

# Test your code below, inside the if statement
if __name__ == "__main__":
    print(get_number_of_a())
    print(get_number_of_z())
    print(get_number_of_percent())
    print(get_number_of_char("a"))
