stringGlobal="global string"
def functionMain():
    stringParent="parent string"
    print("inside the main function\t%s"%stringGlobal)       #calling global variable
    print("inside the main function\t%s" % stringParent)     #calling the variable in the same level
    #print("inside the main function\t%s" % stringChild)     #error occurs in case calling the variable lower-level
    def functionChild():
        stringChild="child string"
        print("inside the child function\t%s"%stringGlobal)    #calling global variable
        print("inside the child function\t%s" % stringParent)  #calling variable in the upper-level
        print("inside the child function\t%s" % stringChild)   #calling the variable in the same level

functionChild()