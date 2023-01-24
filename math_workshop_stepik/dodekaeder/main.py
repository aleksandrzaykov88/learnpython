# На вход программа получает 1 строку - длину ребра додекаэдра.
# Используя формулы из Wiki найдите площадь поверхности и объём фигуры.
# Ответ округлите до 2 знака после запятой.

import math

inputSide = 1

# Отыщем площадь
dodekaeder_S = 3*math.pow(inputSide, 2)*math.sqrt(5*(5+2*math.sqrt(5)))
print(round(dodekaeder_S, 2))

# И объём
dodekaeder_V = (math.pow(inputSide, 3)/4)*(15 + 7*math.sqrt(5))
print(round(dodekaeder_V, 2))