import random
import numpy as np
import time

tim = 0
count = 0
for i in range(100):


  M = 3
  x1mm = [10, 40]
  x2mm = [-30, 45]
  x3mm = [-30, -10]
  # print('x1_min =', x1mm[0], ', x1_max =', x1mm[1])
  # print('x2_min =', x2mm[0], ', x2_max =', x2mm[1])
  # print('x3_min =', x3mm[0], ', x3_max =', x3mm[1])
  # print('------------------------------------------------')
  
  
  x0 = [1, 1, 1, 1]
  x1 = [-1, -1, 1, 1]
  x2 = [-1, 1, -1, 1]
  x3 = [-1, 1, 1, -1]
  # print('x0:', x0)
  # print('x1:', x1)
  # print('x2:', x2)
  # print('x3:', x3)
  # print('------------------------------------------------')
  
  
  X1 = [10, 10, 40, 40]
  X2 = [-30, 45, -30, 45]
  X3 = [-30, -10, -10, -30]
  # print('X1:', X1)
  # print('X2:', X2)
  # print('X3:', X3)
  # print('------------------------------------------------')
  
  
  x_ser_max = (max(X1) + max(X2) + max(X3)) / 3
  x_ser_min = (min(X1) + min(X2) + min(X3)) / 3
  # print('Середнє значення максимумів Х:', x_ser_max)
  # print('Середнє значення мінімумів Х:', x_ser_min)
  # print('------------------------------------------------')
  
  
  y_Max = int(200 + x_ser_max)
  y_Min = int(200 + x_ser_min)
  # print('Максимум У:',y_Max)
  # print('Мінімум У:',y_Min)
  # print('------------------------------------------------')


  y1 = [random.randint(y_Min, y_Max) for i in range(4)]
  y2 = [random.randint(y_Min, y_Max) for i in range(4)]
  y3 = [random.randint(y_Min, y_Max) for i in range(4)]
  # print('y1:', y1)
  # print('y2:', y2)
  # print('y3:', y3)
  # print('------------------------------------------------')
  
  
  y_ser_arr = [(y1[i] + y2[i] + y3[i]) / 3 for i in range(4)]
  # print('Середні значення У:', y_ser_arr)
  # print('------------------------------------------------')
  
  
  mx1 = np.average(X1)
  mx2 = np.average(X2)
  mx3 = np.average(X3)
  my = np.average(y_ser_arr)
  # print('mx1 =', mx1)
  # print('mx2 =', mx2)
  # print('mx3 =', mx3)
  # print('my =', my)
  # print('------------------------------------------------')
  
  a1 = sum([X1[i] * y_ser_arr[i] for i in range(4)]) / 4
  a2 = sum([X2[i] * y_ser_arr[i] for i in range(4)]) / 4
  a3 = sum([X3[i] * y_ser_arr[i] for i in range(4)]) / 4
  # print('a1 =', a1)
  # print('a2 =', a2)
  # print('a3 =', a3)
  # print('------------------------------------------------')
  
  a11 = sum([i * i for i in X1]) / 4
  a22 = sum([i * i for i in X2]) / 4
  a33 = sum([i * i for i in X3]) / 4
  # print('a11 =', a11)
  # print('a22 =', a22)
  # print('a33 =', a33)
  # print('------------------------------------------------')
  
  a12 = sum([X1[i] * X2[i] for i in range(4)]) / 4
  a13 = sum([X1[i] * X3[i] for i in range(4)]) / 4
  a23 = sum([X2[i] * X3[i] for i in range(4)]) / 4
  a21 = a12
  a31 = a13
  a32 = a23
  # print('a12 =', a12)
  # print('a13 =', a13)
  # print('a23 =', a23)
  # print('a21 =', a21)
  # print('a31 =', a31)
  # print('a32 =', a32)
  # print('--------------------------------------------------------------------------------------------------')


  b0 = np.linalg.det([[my, mx1, mx2, mx3],
            [a1, a11, a12, a13],
            [a2, a21, a22, a23],
            [a3, a31, a32, a33]]) / np.linalg.det([[1, mx1, mx2, mx3],
                                        [mx1, a11, a12, a13],
                                        [mx2, a21, a22, a23],
                                        [mx3, a31, a32, a33]])
  b1 = np.linalg.det([[1, my, mx2, mx3],
            [mx1, a1, a12, a13],
            [mx2, a2, a22, a23],
            [mx3, a3, a32, a33]]) / np.linalg.det([[1, mx1, mx2, mx3],
                                        [mx1, a11, a12, a13],
                                        [mx2, a21, a22, a23],
                                        [mx3, a31, a32, a33]])
  b2 = np.linalg.det([[1, mx1, my, mx3],
            [mx1, a11, a1, a13],
            [mx2, a21, a2, a23],
            [mx3, a31, a3, a33]]) / np.linalg.det([[1, mx1, mx2, mx3],
                                        [mx1, a11, a12, a13],
                                        [mx2, a21, a22, a23],
                                        [mx3, a31, a32, a33]])
  b3 = np.linalg.det([[1, mx1, mx2, my],
            [mx1, a11, a12, a1],
            [mx2, a21, a22, a2],
            [mx3, a31, a32, a3]]) / np.linalg.det([[1, mx1, mx2, mx3],
                                        [mx1, a11, a12, a13],
                                        [mx2, a21, a22, a23],
                                        [mx3, a31, a32, a33]])

  # print(f'y = {b0} + {b1}*x1 + {b2}*x2 + {b3}*x3')


  # print('!!!----------------------------------------------------------------------------!!!')
  # print('Перевірка:')
  for i in range(4):
      y = b0 + b1 * X1[i] + b2 * X2[i] + b3 * X3[i]
  #     print('y =', y)
  # print('!!!----------------------------------------------------------------------------!!!')


  # print('Перевірка однорідності дисперсії за критерієм Кохрена')

  dispersion = [((y1[i] - y_ser_arr[i]) ** 2 + (y2[i] - y_ser_arr[i]) ** 2 + (y3[i] - y_ser_arr[i]) ** 2) / 3 for i in range(4)]
  # print('Дисперсії:', dispersion)

  gp = max(dispersion) / sum(dispersion)
  # print('Gp =', gp)
  # print('Gт = 0.7679')


  if gp < 0.7679:
    count +=1
    # print('Дисперсія однорідна')
    # print('---------------------------------------------------------------------------')

    # print('Оцінка значимості коефіцієнтів регресії за критерієм Стьюдента')

    s2b = sum(dispersion) / 4
    s2bs = s2b / 4 * M
    sb = s2bs ** (1/2)

    beta0 = sum([y_ser_arr[i] * x0[i] for i in range(4)]) / 4
    beta1 = sum([y_ser_arr[i] * x1[i] for i in range(4)]) / 4
    beta2 = sum([y_ser_arr[i] * x2[i] for i in range(4)]) / 4
    beta3 = sum([y_ser_arr[i] * x3[i] for i in range(4)]) / 4

    beta_arr = [beta0, beta1, beta2, beta3]
    t_arr = [abs(beta_arr[i]) / sb for i in range(4)]
    # print('beta0 =', beta0)
    # print('beta1 =', beta1)
    # print('beta2 =', beta2)
    # print('beta3 =', beta3)
    # print()
    # print('t0 =', t_arr[0])
    # print('t1 =', t_arr[1])
    # print('t2 =', t_arr[2])
    # print('t3 =', t_arr[3])
    # print()
    # print('tтабл = 2.306')
    # print('------------------------------------------------------------------------------------')

    ind = []


    start = time.perf_counter()

    for i, v in enumerate(t_arr):
      if t_arr[i] > 2.306:
          ind.append(i)

    end = time.perf_counter()
    tim += end-start



      # else:
      #     print(f'Коефіцієнт b{i} приймаємо не значним при рівні значимості 0.05')

    # print()
    b_list = [b0, b1, b2, b3]
    # print(f'y = b{ind[0]}')
    # print()


    b_res = [b_list[ind[0]] for i in range(4)]
    # for i in b_res:
    #   print(f'y = {i}')

    # print('----------------------------------------------------------------------------')


    # print('Критерій Фішера')

    d = 1
    # print('d =', d)

    s2_ad = M * sum([(y_ser_arr[i] - b_res[i]) ** 2 for i in range(4)]) / (4 - d)
    fp = s2_ad / s2b
    # print('Fp =', fp)
    # print('Ft = 4.5')


  #   if fp > 4.5:
  #       print('Рівняння регресії неадекватно оригіналу при рівні значимості 0.05')
  #   else:
  #       print('Рівняння регресії адекватно оригіналу при рівні значимості 0.05')
  # else:
  #   print('Дисперсія неоднорідна')
    # print('---------------------------------------------------------------------------')
print('Кількість однорідних дисперсій:', count)
print('Загальний час обчислення значимих коефіцієнтів:', tim)
print('Середній час обчислення значимих коефіцієнтів:', tim/count)