"""
                            Print letter 'S' using star pattern
                                         (Only for fun)            
"""

for row in range(7):
        if row==0 or row==3 or row==6:
            print(" ***")
        if row==1 or row==2:
            print("*")
        if row==4 or row==5:
            print("    *")
