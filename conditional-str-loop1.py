for i in range(2):
    print(i)

print("First loop:")
for a in range(1,11):
    print(a)

print("Second loop:")

#Write a loop here that prints the numbers from -5 to 5,
#inclusive. Print each number on a separate line.
for b in range(-5,6):
    print(b)

print("Third loop:")

#Write a loop here that prints the even numbers only from 1
#to 20, inclusive. Print each number on a separate line.
#
#Hint: There are two ways to do this. You can use the syntax
#for the range() function shown in the multiple-choice
#problem above, or you can use a conditional with a modulus
#operator to determine whether or not to print.

for c in range(1, 21):
    if(c%2 == 0):
        print(c)

sum=0

for num in range(1,11):
    nextNum = int(input("Enter number # "+str(num)+" :"))
    sum += nextNum

print("sum of the numbers are : "+str(sum))
print("avr of the numbers are : "+str(sum/10))