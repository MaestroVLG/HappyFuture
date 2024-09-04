'''Библиотека pillow'''

from PIL import Image, ImageFilter
import os

from PIL.ImageFile import ImageFile

#Загрузка изображения из папки и отображене информации о нем
papka = 'C:\\Users\\SOGAZ-Med\\Pictures\\цель'


image: ImageFile= Image.open(os.path.join(papka, 'жопка справа.jpg'))
print(image.format, image.size, image.mode)


#Перевод изображения в черно-белый формат, изменение размера и применение фильтра + вывод изображения
image = image.convert('L').resize((900, 900)).filter(ImageFilter.BLUR).show()

#Сохранение изменённого изображенияв в папку
image = Image.save(os.path.join(papka, 'жопка справа_2.jpg'))




#######################################################################

'''Библиотека Matplotlib'''

import matplotlib.pyplot as plt
import numpy as np

# Создать массив данных
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Построить линию
plt.plot(x, y)

# Установить метки осей и заголовок
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')

# Отобразить график
plt.show()



