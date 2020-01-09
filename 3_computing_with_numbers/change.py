# change.py
# A program to calculate the value of some change in Kenyan Shillings
def main () :
    print ("Change Counter")
    print ()
    print ("Please enter the count of each coin type. ")
    OneCents = int (input ("1 cents: ") )
    FiveCents = int (input ("5 cents: ") )
    TenCents = int (input ("10 cents: ") )
    TwentyCents = int (input ("20 cents: ") )
    FiftyCents = int (input ("50 cents: ") )
    OneBobs = int (input ("1 Shilling: ") )
    FiveBobs = int (input ("5 Shillings: ") )
    TenBobs = int (input ("10Shillings: ") )
    TwentyBobs = int (input ("20 Shillings: ") )
    total = (OneCents * .01 + FiveCents * .05 + TenCents * .1 + TwentyCents * .2 + FiftyCents * .5 + OneBobs * 1 + FiveBobs * 5 + TenBobs * 10 + TwentyBobs * 20 ) 
    total = round(total,2)
    print ()
    print ("The total value of your change is KES ", total)
    print()
    input ( " Press <Enter> to quit " )
    
main ()