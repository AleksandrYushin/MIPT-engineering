#График (точки из файла)
y=[]
with open('data.txt', 'r') as file:
    arr=file.readlines()
    for i in arr:
        a = ''.join(i)
        y.append(float(a))
s=[]
with open('settings.txt', 'r') as file:
    arr=file.readlines()
    for i in arr:
        a = ''.join(i)
        s.append(float(a))
#Импорт и стили
from matplotlib import pyplot
import matplotlib.pyplot as plt

plt.minorticks_on()
plt.title('Процесс заряда и разряда кондесатора в RC-цепочке')
plt.ylabel('Напрежение U, В')
plt.xlabel('Время t, с')
plt.xlim([0, 90])
plt.ylim([0, 3.3])
plt.grid(which='major', linestyle='-.')
plt.grid(which='minor', linestyle=':')
plt.tight_layout()
plt.text(60, 2.4,'Время зарядки: 41.72')
plt.text(60, 2.0,'Время разрядки: 40.05')

#Рисование крестов
x=[]
for i in range(len(y)):
    x.append(i/s[0])
plt.plot(x, y,'-', color='g', label='U(t)')

plt.scatter(x[::30], y[::30], color='r', label='Эксперементальные точки')

plt.legend(fontsize=14)
plt.show()