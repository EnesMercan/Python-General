print("_" * 40)

#floating point
number1=3.1415
print("number1=3.1415")
print("This is a \'floating point\'\t%f" %number1)

print("_" * 40)

#integer
number2=123123123
print("number2=123123123")
print("This is an \'integer\'\t%d" %number2)

print("_" * 40)

#string
name = "enes mercan"
print("name = \"enes mercan\"")
print("This is a \'string\'\t%s" %name)

print("_" * 40)

#list
variable1=[1, 2, 3, '2', 'zxcvxz', "qwdqd", (1, '10', name), name]
print("variable1=[1, 2, 3, \'2\', \'zxcvxz\', \"qwdqd\", (1, '10', name), name]")
print("This is (below) a \'list\'\n",variable1)

print("_" * 40)

#tuple
variable2 = (1, 2, (1,'2', "enes mercan", name, variable1))
print("This is a \'tuple\'\n",variable2)

print("_" * 40)

#dict
variable3 = {'enes':92, 'mercan':12, 'ahmet':'otuz'}
print("This is a \'dictionary\'\n",variable3)

print("_" * 40)

#set
variable4={1,2,3,4,1,3,4,5,8,10,123}
print("set =  \'\'",variable4)
variable4= set()
print("This is a \'set\'\n",variable4)

print("_" * 40)


#standart function
def function(number1 ,number2) :
    return number1 + number2
result = function(20, 30)
print("standart function declaration\n"
      "def function(number1 ,number2) :\n"
      "\treturn number1 + number2\n"
      "result = function(20, 30)\n" 
      "^ (result=%d)" %result)
print("_" * 40)

#_________________________________________________________________________________________#

# list
print("\n_________________________________________\n")

myList = [1, 'abcd', ('c', 1, "wnwa")]
mySecondList = [1, '9', 'abcsad', myList, (1, 'asd'), "enes mefrc n"]

print("myList=",myList)
print("myScondList=",mySecondList)

print("\n")

for m in range(6):
    print("mySecondList[%d]\t" % m)
    print(mySecondList[m], "\t", type(mySecondList[m]))

del myList
del mySecondList

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print("\nlist1\t", list1)
print("\nlist2\t", list2)
print("\nlist3=list1+list2\t", list3)

del list2, list3

# string
print("\n_________________________________________\n")

name = input("Hello!What's your name?\n")
print("\nHello", name)
surname = input("So, What\'s your surname?\n")
print("Alright!Gotcha!")
print("\nyour name :\t", name, "\nyour surname :\t", surname, "\nyour full name :\t", (name + " " + surname))
print("\nNice to meet you!")
age = 0
age = int(input("\nHow old are you?\n"))
print("\nHimmm. Your age is %d" % age)


# tuple
print("\n_________________________________________\n")

demet=("enes",'mercan',1,'2',list1,('enes',1,'xyzx'))
print("\ndemet = ",demet)
print("\ntype of the \"demet\" is :\t",type(demet),"\n")

for m in range(6):
    print("demet[%d]\t"%m,demet[m],"\t\ttype:\t",type(demet[m]))


# dics
print("\n_________________________________________\n")

notlar={'enes':90,'mehmet':23,'bok':91}
print("\nnotlar = ",notlar)
print("\ntype of the notlar is :\t",type(notlar))
print("\nnotlar[\'enes\'] :\t",notlar['enes'])
print("\nnotlar[\'mehmet\'] :\t",notlar['mehmet'])
print("\nnotlar[\'bok\'] :\t",notlar['bok'])
strng=str(input("Which person do you wanna delete?"))
del notlar[strng]
print("\n",notlar)


# sets
print("\n_________________________________________\n")

kume1=set()
kume1={0,1,2,3,4,5,6,7,8,2}
print("\nkume1=",kume1,"\ntype of the \'kume\' is :\t",type(kume1))
number = int(input("search a number in \'kume1\'"))
test = number in kume1
if test == 1:
    print(number,"has been founded!")
else:
    print(number,"has not been founded!")