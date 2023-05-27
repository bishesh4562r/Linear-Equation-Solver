global consistent
consistent = True

class Arr():
    def __init__(self,lst) -> None:
        self.lst=lst
        self.length=len(lst)
    
    def __mul__(self,k):
        result=[]
        for i in range(self.length):
            result.append(k*self.lst[i])
        return Arr(result)

    def __add__(self,other):
        result=[]
        if self.length==other.length:
            for i in range(self.length):
                result.append(self.lst[i]+other.lst[i])
        return Arr(result)
    def __sub__(self,other):
        result=[]
        if self.length==other.length:
            for i in range(self.length):
                result.append(self.lst[i]-other.lst[i])
        return Arr(result)
    def __truediv__(self,k):
        result=[]
        for i in range(self.length):
            result.append(self.lst[i]/k)
        return Arr(result)
    def crct(self):
        for i in range(self.length):
            if i!=self.length-1:
                if self.lst[i]<0:
                    self.lst[i]*=-1

def inf(arr):
    for each in arr:
        if set(each.lst)=={0}:
            return True
        
            break
def nos(arr):
    global consistent
    for each in arr:
        const=each.lst.pop(each.length-1)
        if const!=0 and set(each.lst)=={0}:
            consistent=False
            return True
            break
        
                        
n=int(input("Enter the no of unknowns  "))
ag_m=[]
for i in range(n):
    pre=[]
    for j in range(n+1):
        pre.append(None)
    ag_m.append(Arr(pre))

for i in range(len(ag_m)):
    print(f"For equation {i+1}")
    for j in range(ag_m[i].length) :
        if j!=ag_m[i].length-1:
            ag_m[i].lst[j]=(float(input(f"Enter the coefficient of x{j+1}\t")))
        else:
            ag_m[i].lst[j]=(float(input(f"Enter the constant term for equation {i+1}\t")))

print("The augmented matrix of the given system of linear equation is \n")
for each in ag_m:
    print(each.lst)


print("\n")
for i in range(len(ag_m)):
    if ag_m[i].lst[i]==0 and i!=ag_m[i].length-1:
        ag_m[i],ag_m[i+1]=ag_m[i+1],ag_m[i]

for i in range(len(ag_m)):
    if ag_m[i].lst[i]!=0:
        k=ag_m[i].lst[i]
        ag_m[i]=ag_m[i]/k
        for ii in range(len(ag_m)):
            if ii!=i:
                kk=ag_m[ii].lst[i]
                ag_m[ii]=ag_m[ii]-ag_m[i]*kk

        
for i in range(len(ag_m)):
    ag_m[i].crct()

for each in ag_m:
    print(each.lst)            

for i in range(len(ag_m)):
    print(f"x{i+1} = {ag_m[i].lst[ag_m[i].length-1]}")


if nos(ag_m):
    print("No solution")
if inf(ag_m):
    print("Infinitely many solution")    
if consistent:
    print("The system is consistent")

    

                

