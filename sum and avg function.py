def sum_avg(n:int):
    sum=0
    for i in range(i,n+1):
        sum=sum+i

        print('sum is',sum)
        avg=sum/n
        print('average is',avg)

        n=int(input('enter value of n'))
        sum_avg(n)
