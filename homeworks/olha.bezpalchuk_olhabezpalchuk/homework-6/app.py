from Cake import Cake
from WeddingCake import WeddingCake
from converter import *

basic_cake = Cake('Basic cake', ['cream', 'dough'], 10)
print(basic_cake)

esterhazy = Cake('Esterhazy', ['buttercream', 'cognac', 'vanilla', 'almond meringue dough'], 20)
esterhazy.change_cooking_method("buttercream spice with cognac and vanilla, \
 sandwich it between 4 or 5 layers of almond meringue dough")
print(esterhazy)
print(esterhazy.cooking_method)

croquembouche = WeddingCake('Croquembouche', ['4 batches of profiteroles', '4 cups of caster sugar', 'water'],
                            30, ['silver cachous', '2 caramel hearts'])
croquembouche.change_cooking_method("Stir sugar and water (3 to 1) and make toffee. Place profiteroles in \
 pyramid manner, use toffee and hot water to fix them. Pour pyramid with remain toffee and beautify.")

print(croquembouche)
print(croquembouche.cooking_method)

print('-------------------------------------')
print(croquembouche.__dict__)
print('---')
dic = croquembouche.__dict__
print(dic.keys())
print('---')
print(croquembouche.__module__)
print('---')
obj_to_json([basic_cake, esterhazy, croquembouche], 'cakes.json')
obj_to_xml([basic_cake, esterhazy, croquembouche], 'cakes.xml')
