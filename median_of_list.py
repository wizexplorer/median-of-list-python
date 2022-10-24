print("|-------------------------EXPERIMENT NO.25-----------------------------|")
print("|                CALCULATING MEDIAN VALUE OF A LIST                    |")
print("|----------------------------------------------------------------------|")
L=eval(input("                    Enter the list : "))
print("*"*72)
L.sort()
n=len(L)
mid_num=(n-1)//2
if n%2!=0:
    print("                            Median :",L[mid_num])
if n%2==0:
    a=L[mid_num]
    b=L[(n+1)//2]
    median= (a+b)/2
    print("                            Median :", median)
