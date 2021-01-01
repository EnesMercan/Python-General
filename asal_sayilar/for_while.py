max = int(input("input a number\n"))

for i in range(0,max):
    if i == 0:
        continue
    if (i == 1) or (i == 2) or (i == 3):
        print(i)
        continue
    for j in range(2,i-1):
        if i % j == 0 :
            #print("code:1 for i,j %d,%d" %(i,j)) #control panel
            break
        elif j == (i-2) :
            print(i)