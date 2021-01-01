number1 = 0
number2 = 0
number3 = 0

number1 = int(input("\nplease input a fucking number : \n"))
number2 = int(input("\nplease input another number : \n"))
number3 = int(input("\nplease input the last fucking number : \n"))

if number1 > number2 :
    if number1 > number3 :
        print("\nthe biggest number is \t%6d" %number1)

        if number3 > number2 :
            print("\nthe smallest number is \t%6d" %number2)
    else :
        print("\nthe smallest number is \t%6d" %number2)
        print("\nthe biggest number is \t%6d" %number3)
else :
    if number2 > number3 :
        print("\nthe biggest number is \t%6d" % number2)

        if number3 > number1 :
            print("\nthe smallset number is\t %6d" %number1)
    else :
        print("\nthe biggest number is \t%6d" % number3)
        print("\nthe smallest number is \t%6d" %number1)

