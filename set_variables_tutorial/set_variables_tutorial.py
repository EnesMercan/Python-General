ornek = {1,2,3,4,1,2,1,3,4,1,"enes","mercan", "enes"}

print("_" * 80)
print("Welocome to \'set\' tutorial !")
print("_" * 80)
print("\nthis is a normal set :")
print("ornek = {1,2,3,4,1,2,1,3,4,1,\'enes\',\'mercan\', \'enes\'} ")
print("_" * 80)
print("\nHowever, complier automatically reformat it as :")
print("ornek = " , ornek)

print("_" * 80)
print("\nBecause, it's not allowed to store the same datas !")
print("_" * 80)

print("\n")
print("_" * 80)
print("Set yapilarinin ozellikleri :\n")
print("* elemanlari suslu parantezler arasina alinilir")
print("* sirasiz elemanlar kolleksiyonudur")
print("* elemanlara erisim icin index'leri yoktur")
print("* elemanlari tekildir (uniqe)")
print("*** elemanlari degistirilemez (immutable)")
print("* matematiksel kume islemlerini destekler")

print("_" * 80)
print("\nk = {1, 2, 3}\t...\t#Gecerli kume")
print("\nk = {1, 2.123, \'python\', (10, 20, 30)}\t...\t" , "#Gecerli kume")
print("\nk = {1, 11, [20, 30]}\t...\t" , "#Gecersiz kume. eleman olarak \'list\' kabul etmez")
print("\nk = {0,1,2,3,4,5}\t...\t" , "len(k)=6" )

print("\nk = {0, 1, 2, 3, 4, 5, 1}\t\t" , "k[1]\t\t" , "#hata mesaji verir. indis kullanilmaz")

s = "kumelerde indis bulunmaz"
k = set(s)
print("\ns = \"kumelerde indis bulunmaz\"\nk = set(s)\t...\t\t#set(s) string nesnesini elemanlarina ayirir, tekrarlananlari siler ve siralar\nk - > " , k)

myTuple = (1,2,3,4,5,6,2,2,4,1,23,4,5,12,3)
k = set(myTuple)
print("\nmyTuple = (1,2,3,4,5,6,2,2,4,1,23,4,5,12,3)\t\t",
      type(myTuple),
      "\nk = set(myTuple)\t...\t\t#set(s) \'tuple\' nesnesini elemanlarina ayirir, tekrarlananlari siler ve siralar\nk - > " ,
      k ,
      "\t\t" ,
      type(k)
      )

myList = [1,2,3,4,5,6,2,2,1,4,23,4,5,12,3]
k = set(myList)
print("\nmyList = [1,2,3,4,5,6,2,2,4,1,23,4,5,12,3]\t\t",
      type(myList),
      "\nk = set(myList)\t...\t\t#set(s) \'list\' nesnesini elemanlarina ayirir, tekrarlananlari siler ve siralar\nk - > " , k ,
      "\t\t" ,
      type(myList)
      )

print("_" * 90)
print("\nBazi kume (set) metodlari :")
print("\n")