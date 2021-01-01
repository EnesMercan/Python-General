tuple1 = (1, '12', ["list", 1], 3.1415)  #this is a typical tuple
tuple2 = (2, tuple1, 'enes')            #this is a typical tuple

print("_" * 50)
print("\nthose are below typical \'tuple\' iterations:")
print("tuple1=" , tuple1)
print("tuple2=" , tuple2)

print("_" * 50)
print("\nnow les't examine variables :")

count = 0
for word in tuple1 :
    print("%d.data  -->\t"%(count+1) ,"tuple1[%d]=" % count ,word , "\t\t" , type(word))
    count+=1

print("_" * 50)
print("\nyeni tuple olusturalim:")
print("tuple3 = tuple1 + tuple2")
tuple3 = tuple1 + tuple2
print(tuple3)

print("_" * 50)
print("\ntuple\'larin ozellikleri :")
print("* parantez icinde yazilirlar \'()\'")
print("* indisleri sifirdan baslar")
print("* elemanlari degistirilemez (immutable)")
print("* dilimlenebilir (sliceable)")
print("* ic ice gecebilir (nestable)")
print("* her turle veri yapisini saklayabilir")

print("_" * 50)
print("\n33 in (1, 2, 3, 10)\t\t" , (33 in (1, 2, 3, 10)))
print("\n10 in (1, 2, 3, 10)\t\t" , (10 in (1, 2, 3, 10)))

print("_" * 50)
print("\npacking and unpacking")
newTuple = (1,2,3,4,'enes')
(a,b,c,d,e) = newTuple
print("newTuple = (1,2,3,4,'enes')","\t",
      "(a,b,c,d,e) = newTuple"
      )
print("a=",a,"\t",type(a),"\nb=",b,"\t",type(b),"\nc=",c,"\t",type(c),"\nd=",d,"\t",type(d),"\ne=",e,"\t",type(e))

print("_" * 50)
print("\nfonksiyonlar \'tuple\' tipinde veri dondurebilir:")
print("\n",
      "def function(a, b) :",
      "\n    return (a, b)",
      "\nprint(function(a,b))\n\n",
      )
def function(a, b) :
    return (a, b)
a = int (input("input a number\n"))
b = int (input("input a number\n"))
print(function(a,b) , "\t" , type(function(a, b)) )

print("_" * 50)
print("\ntuple icindeki tuple'a ulasmak :")
tuple4 = (1,2,("enes",1,3,3.11415))
print("\ntuple =" , tuple4 )

count = 0
for word in tuple4[2] :
    print("tuple[2][%d] = " % count , " " , word , "\t" , type(word))
    count+=1


print("_" * 90)
print("\n*  Elemanlari degistirilemez oldugundan listeye gore biraz daha hizli calisir")
print("\n*  Elemanlari degistirilemez oldugu icin degismemesi gereken veri kullanimi gereken yerlerde avantaj saglar")
print("\n*  \'Demet\' elemanlari sozluk veri yapiularinda anahtar olarak kullanilabilir. Oysa listeler b8u amacla kullanilamaz.")
print("\n*  Yazilimcilarin genel egilimi benzer elemanlar sozkonusu oldugunda \'list\'e , farkli tip elemanlar sozkonusu oldugunda ise \'demet\' veri yapilarinin kullanilmasidir.")
