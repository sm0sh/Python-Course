I1=int(input("Enter INT201 Marks : "))
I2=int(input("Enter INT501 Marks : "))
I3=int(input("Enter CSE841 Marks : "))
I4=int(input("Enter CSE101 Marks : "))
 
Total= I1+I2+I3+I4
P=int((Total/400)*100)
print(P)
if P>=75:
     print("Distinction")
elif P<75 & P>60:
     print("First Division")
elif P<59 & P>50:
     print("Second Division")
elif P<49 & P>40:
     print("Third Division")
else:
     print("FAIL")         
