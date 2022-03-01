#         Question 1
from unicodedata import name


print('       Question 1\n')
 

def hanoi(num_disks,source,destination,temp):
    if num_disks<=0:
        print("Input should be atleast 1")
    if num_disks==1:
        print("Move disk 1 from SOURCE:",source,"to DESTINATION:",destination)
        return
    hanoi(num_disks-1,source,temp,destination)
    print("Move disk",num_disks,"from SOURCE:",source,"to DESTINATION:",destination)
    hanoi(num_disks-1,temp,destination,source)


num_disks=int(input("Enter number of disks: "))

source=input("Name of source rod: ")
destination=input("Name of destination rod: ")
temp=input("Name of 3rd rod: ")

hanoi(num_disks,source,destination,temp)









#         Question 2
print('       Question 2\n')



def fact(num):
    if num<=1 :
      return 1 
     
    else :  
      return  num*fact(num-1)

def ncr( n , r ):
    nCr = fact(n)//(fact(r) * fact(n-r))
    return nCr 

n_rows = int ( input ( 'Enter the no of rows:'))
# A. Iteration>>>
print("Pascal's Triangle using Iteration: ")


for row  in range (n_rows):
    for space in range (n_rows-row):
        print( " " , end="")
    for coloumn in range (row+1):
        print( ncr(row ,coloumn) , end=" ")
    print( "\n")

# B. Recursion>>>
print("Pascal's Triangle using Recursion: ")

def pascal_triangle(n_rows,row):
    if n_rows==0:
        return
    for space in range(n_rows-1):
        print(" ",end="")
    row+=1
    column=0
    while column<=row:
        print( ncr(row,column),end=" ")
        column+=1
    print("\n")

    pascal_triangle(n_rows-1,row)

pascal_triangle(n_rows,-1)









#         Question 3
print('       Question 3\n')

dividend=int(input("Enter Dividend: "))
divisor=int(input("Enter Divisor: "))

result=divmod(dividend,divisor)
print("(Quotient,Remainder) ->",result)

# A>>>
print("A) Is the function 'divmod' callable: ",callable(divmod))

# B>>>
if result[0]==0 and result[1]==0:
    print("B) All values are zero: ",True)
else:
    print("C) All values are zero: ",False)

# C>>>
result=result+(4,5,6)
new_tupple=()
for i in range(len(result)):
    if result[i]>4:
        new_tupple=new_tupple+(result[i],)
print(new_tupple)
# D>>>
res=set(result)
print("D) Set:",res)

# E>>>
frozenset(res)
print("E) Immutable Set:",res)

# F>>>
print("F) The maximum value in the set is:",max(res),"and its hash value is:",hash(str(max(res))))









#         Question 4
print('       Question 4\n')

class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        print("Student created: ",name,"\nRoll no,:",roll_no)
    def __del__(self):
        print(self,"deleted")
print("A)")
std1=Student("Pranzal",48)
std2=Student("XYZ",123)

print("B) Deleting XYZ...")
del std2












#         Question 4
print('       Question 4\n')

class employee:
    def __init__(self,emp_num,emp_name,salary):
        self.emp_num=emp_num
        self.emp_name=emp_name
        self.salary=salary
    def info(self):
        print("Employee:",self.emp_name,"\nSalary:",self.salary,"\n")
    def __del__(self):
        print("Employee:",self,"deleted")

emp1=employee(1,"Mehak",40000)
emp2=employee(2,"Ashok",50000)
emp3=employee(3,"Viren",60000)

emp1.info()
emp2.info()
emp3.info()

# A>>>
emp1.salary=70000
print("A) Mehak's employee details after update:")
emp1.info()

# B>>>
print("B) Deleting Viren's details...")
del emp3