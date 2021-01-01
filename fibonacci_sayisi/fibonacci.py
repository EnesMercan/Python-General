print("Welcome to fibonacci algorithim!")
print("Which way do you wanna choose?")
choise=str(input("\nfunction\nclassic\n"))

if choise == 'function' :
    def fibonacci(max) :
        k = 1
        l = 1
        while max >= 0 :
            result = k + l
            print("\n\t%d\t+\t%d\t=\t%d" % (k, l, result))
            k = l
            l = result
            max-=1
    fibonacci(int(input("max number?\n")))

elif choise == "classic":
    i = 1
    j = 1
    for count in range(100):
        result = i + j
        print("\n\t%d\t+\t%d\t=\t%d" % (i, j, result))
        i = j
        j = result

else :
    print("Incorrect input!")