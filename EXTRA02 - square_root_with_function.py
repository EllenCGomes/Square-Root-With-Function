import math
# receive values
def main():
    a = float(input("Enter 'a' value:"))
    b = float(input("Enter 'b' value:"))
    c = float(input("Enter 'c' value:"))
    print_sqrt(a, b, c)

# calculate delta
def delta(a,b,c): 
    return (b**2)-(4*a*c)      

# calculate square roots
def print_sqrt(a, b, c):
    d = delta(a,b,c)
    sqrt1 = (-b + math.sqrt(d))/(2*a)
    sqrt2 = (-b - math.sqrt(delta(a,b,c)))/(2*a)
    
    if d == 0:
        print("the solution for this equation is", sqrt1)
    else:
        if d < 0:
            print("this equation has an imaginary root")
        else:  
            if sqrt1<sqrt2:   
                print("the roots for this equation are {} and {}".format(sqrt1, sqrt2))
            else:
                print("the roots for this equation are {} and {}".format(sqrt2, sqrt1))    
