x=range(50, 100)
for y in x:
    if y%2==1:
        print(y)


#Using while if and continue, print all the numbers that are divisible by 5 between 100 and 200
x=100
y= 200
while x<y:
    x+=1
    if x%5!=0:
      continue
print(x)





