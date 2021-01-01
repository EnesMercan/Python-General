# L I S T E L E R

#listeler her turlu veriyi (tuple, list, string...) icerebilirler.
#tuple ve string nesneleri ile ayni dilimleme ve atlama islemini destekler

#koseli parantez icinde yazilir
#indisleri sifirdan baslar
#elemanlari degistirilebilir (mutable)
#dilimlenebilir (sliceable)
#icice gecebilir (nestable)

#ornek 1 _________________________________________________________________________
print("_" * 60)

print("Asagidaki , standart bir listeye ornektir")    #Asagidaki , standart bir listeye ornektir
liste = [1, '2', "enes", (1, 2, 3), ["enes", 1], {1, 5, 9, 9, 9, 1}, {'enes':90, 'mert':20, 'bok':10}, 3.1415]
print("liste = %s"%liste)
print("\nSimdi bu listedeki verilerin tiplerini inceleyelim:")
for word in liste :
    print(word , "\t" ,type(word))
print("\nuzunluk:\t",len(liste), "\t", "len(liste)")

#ornek 2 _________________________________________________________________________
print("_" * 60)

*popo, ornek = [1, 2, 3, "enes", (1, 2, 3)]
popo = [1,2,3]
ornek = ["enes", (1, 2, 3)]
print("\n%s\n%s"%(popo, ornek))

#ornek 3 _________________________________________________________________________
print("_" * 60)

ilk, *orta, son = [7, 10 ,3 ,2 ,"enes" ,"mercan" ,(1, 2, "bok")]
print("%s\n%s\n%s" % (ilk, orta, son))                              #goruldugu uzere degerler random atandi
                                                                    #bir sonraki ornekte biz atama yapacagiz

#ornek 4 _________________________________________________________________________
print("_" * 60)

ilk, *orta, son = [7, 10 ,3 ,2 ,"enes" ,"mercan" ,(1, 2, "bok")]
ilk = [7, 10]
orta = [3, 2, "enes"]
son = ["mercan", (1, 2, "bok")]
print("%s\n%s\n%s" % (ilk, orta, son))


#ornek 5 _________________________________________________________________________
print("_" * 60)

*parca1, parca2, parca3, parca4 = [7, 10 ,3 ,2 ,"enes" ,"mercan" ,(1, 2, "bok")]
parca1 = [7, 10]
parca2 = [3, 2, "enes"]
parca3 = ["mercan"]
parca4 = [(1, 2, "bok")]

print("%s\n%s\n%s\n%s" % (parca1, parca2, parca3 ,parca4))


#ornek 5 _________________________________________________________________________
print("_" * 60)

mylist = [1, 4, 6, 2, 5, 352, 35, 2, 9 ,8]
print("\nthe original list --> \t" , mylist)
mylist.append(2)
print("\nmylist.append(2) -->\t" , mylist)
print("mylist.count(2) -->\t\t" , mylist.count(2))
mylist.insert(5, "enes")
print("mylist.insert(5, \"enes\") -->\t" , mylist)
mylist.reverse()
print("mylist.reverse() -->\t" , mylist)
del mylist[6]
print("del mylist[5] -->\t" , mylist)
mylist.sort()
print("mylist.sort() -->\t" , mylist)  #you have to delete strings before sorting the list
mylist.insert(5, "enes")
print("mylist.insert(5, \"enes\") -->\t" , mylist)
mylist.remove("enes")
print("mylist.remove('enes') -->\t" , mylist)


#ornek 6 _________________________________________________________________________
print("_" * 60)

newList = list( range(0,11) )
print("newList = list( range(0,11) )\n", "newList =", newList)

#ornek 7 _________________________________________________________________________
print("_" * 60)

def speech(string) :
    if string == 'append':
        return "        isim.append(a)       'a' elemanini listenin sonuna ekler"
    elif string == 'clear':
        return "      isim.clear()        tum elemaninlari siler"
    elif string == 'copy':
        return "      isim.copy()         listenin kopyasini olusturur"
    elif string == 'count':
        return "      isim.count(a)       'isim' listesinde kac 'a' var"
    elif string == 'extend':
        return "      isim.extend(n)       'n' nesnesinin elemanini listenin sonuna ekler"
    elif string == 'index':
        return "      isim.index(n, ilk, son)      'n' nesnesini [ilk,son] araliginda arar"
    elif string == 'insret':
        return "       isim.insert(i,a)      'a' elemanini listenin i. sirasina koyar"
    elif string == 'pop':
        return "            isim.pop()    listenin en son elemanini dondurur ve sonra siler"
    elif string == 'remove':
        return "       isim.remove(a)     ilk buldugu 'a' elemanini siler"
    elif string == 'reverse':
        return "       isim.reverse()     listenin siralamasini ters cevirir"
    elif string == 'sort':
        return "       isim.sort()    icerigi siralar"
    else :
        return "       error code : #1"   #argument ('string') does not match

print("\nsimdi tum metod\'lari listeleyelim\n")
for m in dir(list) :
    if m[0] != '_' :
        print("%s\t\t-->\t%s" %(m, speech(m)))

    else :
        print(m)

#ornek 8 _________________________________________________________________________
print("_" * 60)

print("\npratik bur yontem")
print("\n",
"liste = [10,20,30,40,50,60,70,80]",
"\n(a,b,c,d,e,f,g,h) = liste"
      )

liste = [10,20,30,40,50,60,70,80]
(a,b,c,d,e,f,g,h) = liste
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)