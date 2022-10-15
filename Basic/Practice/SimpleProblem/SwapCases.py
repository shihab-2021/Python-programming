"""
 You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.(don’t use any python built in function)
Example :  pHitrOn.iO presents "Python COuRSe".
Ans : PhITRoN.Io PRENSENTS “pYTHON coUrsE” 
"""
sentence = input()
output = ""
for letter in sentence:
    if letter>='a' and letter<='z':
        output+=chr(ord(letter)-32)
    elif letter>='A' and letter<='Z':
        output+=chr(ord(letter)+32)
    else:
        output+=letter
sentence = output
print(sentence)