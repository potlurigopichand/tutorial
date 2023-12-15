n = 10
if n % 2 == 0:
   print("n is an even number")


   n = 5
if n % 2 == 0:
   print("n is even")
else:
   print("n is odd")


   a = 20
b = 10
c = 15
if a > b:
   if a > c:
      print("a value is big")
   else:
       print("c value is big")
elif b > c:
    print("b value is big")
else:
     print("c is big")


     print("1st example")

lst = [1, 2, 3]
for i in range(len(lst)):
     print(lst[i], end = " \n")
 
print("2nd example")

for j in range(0,5):
    print(j, end = " \n")



    m = 5
i = 0
while i < m:
     print(i, end = " ")
     i = i + 1
print("End")



x = 5

print(x > 3 and x < 10)


x = 5

print(x > 3 or x < 4)


x = 5

print(not(x > 3 and x < 10))


