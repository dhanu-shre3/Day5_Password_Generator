target = int(input()) # Enter a number between 0 and 1000

#step 1= find the even numbers using range function


num = target 
even_sum =  0
for number in range(0, num+1, 2):
    print(number)
    even_sum += number

print(even_sum)