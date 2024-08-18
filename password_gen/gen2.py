import random


def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)


uppercaseLetter1 = chr(random.randint(65, 90))
uppercaseLetter2 = chr(random.randint(65, 90))
uppercaseLetter3 = chr(random.randint(65, 90))
uppercaseLetter4 = chr(random.randint(65, 90))
uppercaseLetter5 = chr(random.randint(65, 90))
uppercaseLetter6 = chr(random.randint(65, 90))
lowercaseLetter7 = chr(random.randint(97, 122))  # Generate a random lowercase letter (ASCII 97-122)
uppercaseLetter8 = chr(random.randint(65, 90))


digit1 = chr(random.randint(48, 57))  # Generate a random digit (ASCII 48-57)
digit2 = chr(random.randint(48, 57))


password = (uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 +
            uppercaseLetter4 + uppercaseLetter5 + uppercaseLetter6 + 
            lowercaseLetter7 + uppercaseLetter8 + digit1 + digit2)

password = shuffle(password)


print(password)
