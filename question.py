#write a program which will find all such numbers which are divisible by 7, but are not a multiple pf 5, between 2000 and 3200, the number should be printed in a comma-separated sequence on a line
list=[]
for a in range (2000,3200):
    if (a%7)==0 and (a%5)!=0:
        list.append(a)
print(list)
