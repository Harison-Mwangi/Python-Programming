# month2 . py
# A program to print the month abbreviation , given its number.

def main():
    # months is a list used as a lookup table
    months = [ " Jan" , " Feb " , "Mar " , "Apr " , " May " , " Jun" ,
    " Jul " , " Aug" , " Sep " , " Oct " , " Nov " , "Dec " ]

    n = int(input("Enter a month number ( 1-12): "))
    print ("The month abbreviation is ", months [n-1] + ".")
    months = [ " January " , " February " , " March" , "April " ,
    " May" , "June " , "July " , "Aug ust " ,
    " September " , " October " , " November " , "December " ]
    
    print("The full month name is ", months[n-1] + ".")

main()