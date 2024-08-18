import random

# A function to shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)


uppercaseLetter1 = chr(random.randint(65, 90))  #(based on ASCII code)
uppercaseLetter2 = chr(random.randint(65, 90))
uppercaseLetter3 = chr(random.randint(65, 90))
uppercaseLetter4 = chr(random.randint(65, 90))
uppercaseLetter5 = chr(random.randint(65, 90))
uppercaseLetter6 = chr(random.randint(65, 90))
uppercaseLetter7 = chr(random.randint(65, 90))
uppercaseLetter8 = chr(random.randint(65, 90))


uppercaseLetter2 = uppercaseLetter2.lower()
uppercaseLetter4 = uppercaseLetter4.lower()
uppercaseLetter6 = uppercaseLetter6.lower()
uppercaseLetter8 = uppercaseLetter8.lower()


password = (uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + 
            uppercaseLetter4 + uppercaseLetter5 + uppercaseLetter6 + 
            uppercaseLetter7 + uppercaseLetter8)

password = shuffle(password)


print(password)
