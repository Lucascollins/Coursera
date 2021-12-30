file_counts = {"jpg": 10,"txt":14, "csv":2,"py":23}
for extension in file_counts:
    print(extension)

for ext,amount in file_counts.items(): # items para interar as informações numerais do dicionario
    print(f"There are {amount} files with the .{ext} extesion")

print(file_counts.keys())
print(file_counts.values())

for value in file_counts.values():
    print(value)


def count_letters(text):

    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter]+= 1
    print( result)

count_letters("AaBbCc")