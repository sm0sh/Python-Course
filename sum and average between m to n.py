m = int(input("Enter a number:"))
n = int(input("Enter a second number:"))
count = 0
for i in range(m,n+1):
    if i%2==0:
        print(i)
        count=count+1
print("total even no",count)        
 
