print("\033c")

num = int(input( "enter a number : " ))

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** 3
    temp = temp // 10

if num == sum:
    print( f"{num} is an Armstrong Number" )

else:
    print( f"{num} is not an Armstrong Number" )