import myModule

result = myModule.topla(20,10)
print(result)

#------------------------------------------

import myModule as mm

sonuc = mm.topla(10,20)
print(sonuc)

#------------------------------------------

from myModule import topla

sayi = topla(12, 18)
print(sayi)

#------------------------------------------

import myModule

new = myModule.myList
print("\n" , new)