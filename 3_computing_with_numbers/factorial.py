# factorial. py
# Program to compute the factorial of a number
# Illustrates for loop with an accumulator

def main () :
    print("This program computes the factorial of the input number.")
    n = int (input ("Please enter a whole number: ") )
    fact = 1
    for factor in range (n,1,-1) :
        fact = fact * factor

    print ("The factorial of", n, "is", fact)
    print()
    input ( " Press <Enter> to quit " )
    
main ()

'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter a number: ")
print(factorial(n))
'''
