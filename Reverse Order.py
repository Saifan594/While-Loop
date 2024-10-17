print( "\033c" )

number = int( input( "enter a number : " ) )

i = number
digit = 0

while i > 0:
    
    i //= 10
    digit += 1

print( f"there are {digit} digit(s) in {number}\n" )