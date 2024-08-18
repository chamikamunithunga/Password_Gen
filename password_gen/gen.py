
import random


def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)


uppercaseLetter1=chr(random.randint(65,90))  #(based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90))
uppercaseLetter3=chr(random.randint(65,90))
uppercaseLetter4=chr(random.randint(65,90))
uppercaseLetter5=chr(random.randint(65,90))
uppercaseLetter6=chr(random.randint(65,90))
lowercaseLetter7=chr(random.randint(65,90))
uppercaseLetter8=chr(random.randint(65,90)) 



password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + uppercaseLetter5 + uppercaseLetter6 +  lowercaseLetter7 + uppercaseLetter8 
password = shuffle(password)


print(password)