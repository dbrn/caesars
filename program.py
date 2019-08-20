# shifting function
def shift_message(array):
    for i in range(len(array)):
        # if the ascii number is between 65 and 90 or 97 and 122 (A-Z or a-z)
        if 65 <= array[i] <= 90 or 97 <= array[i] <= 122:
            #shift it and if it becomes greater than Z or z get back to A or a
            if array[i] + 1 == 91:
                array[i] = 65
            elif array[i] + 1 == 123:
                array[i] = 97
            else:
                array[i] = array[i] + 1
        # if the character is not a letter, ignore it
        else:
            continue
    return array


message = list(input("Enter the sentence to encode: "))
# convert the message into its decimal ascii number
for i in range(len(message)):
    message[i] = ord(message[i])
shift = int(input("Number of shifts: "))
# repeat the shifting algorithm for "shift" times
for i in range(shift):
    message = shift_message(message)
# convert the message back to characters
for i in range(len(message)):
    message[i] = chr(message[i])
# print all the letters in the array with no space in-between
print("".join(message))
