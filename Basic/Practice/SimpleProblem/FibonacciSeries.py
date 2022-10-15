""" 
Display Fibonacci series up to 10 terms
0  1  1  2  3  5  8  13  21  34
"""
num = input()
prev1=0
prev2=1
output = ""
for i in range(int(num)):
    if(i==0):
        output+=str(0)+' '
    elif(i==1):
        output+=str(1)+' '
    else:
        curr = prev1+prev2
        prev1 = prev2
        prev2 = curr
        output+=str(curr)+' '
print(output)
