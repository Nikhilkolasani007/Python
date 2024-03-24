F_no = int(input("Enter the First Number: "))
S_no = int(input("Enter the Second Number: "))
T_no = int(input("Enter the Third Number: "))


def high_num(F_no, S_no, T_no):
    
    if F_no > S_no:
        
        print(str(F_no) + " IS THE HIGHEST NUMBER")
        return F_no
    
    elif S_no > T_no:
        
        print(str(S_no) + " IS THE HIGHEST NUMBER")
        return S_no
    
    else:
        
        print(str(T_no) + " IS THE HIGHEST NUMBER")
        return T_no
    

result = high_num(F_no, S_no, T_no)
print("The highest number is:", result)
