str=input('enter any string')
rev=''
n=len(str)
count=n-1
while(count>=0):
    rev=rev+str[count]
    count=count-1

print('reversed string is:',rev)    

