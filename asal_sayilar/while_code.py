max = int(input("input a number\n"))
i=0
while i <= max:
    counter = 1
    i += 1
    if (i == 1) or (i == 2) :
        print(i)
        continue

    while counter < i:
        counter += 1

        if i % counter == 0:
            counter = i
        elif counter == (i-1):
            print(i)