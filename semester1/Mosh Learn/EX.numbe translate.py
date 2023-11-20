numbers_to_word = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}

input_numbers = input("Phone: ")
output = ""

for number in input_numbers:
    output += numbers_to_word.get(number, "!") + " "
    
print(output)