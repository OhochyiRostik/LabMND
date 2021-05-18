from numpy.linalg import solve
from scipy.stats import f, t
import math
import random
import numpy as np
import time




def Lab6(k):
  m = k
  n = 15
  d = 11

  x1min = 10
  x1max = 40
  x2min = -30
  x2max = 45
  x3min = -30
  x3max = -10

  print("x1 min =", x1min, ", x1 max = ", x1max)
  print("x2 min =", x2min, ", x2 max = ", x2max)
  print("x3 min =", x3min, ", x3 max = ", x3max)
  print("----------------------------------------------------------------------------------")


  
  x01 = (x1max + x1min) / 2
  x02 = (x2max + x2min) / 2
  x03 = (x3max + x3min) / 2
  deltax1 = x1max - x01
  deltax2 = x2max - x02
  deltax3 = x3max - x03


  xn = [[-1, -1, -1, +1, +1, +1, -1, +1, +1, +1],
      [-1, -1, +1, +1, -1, -1, +1, +1, +1, +1],
      [-1, +1, -1, -1, +1, -1, +1, +1, +1, +1],
      [-1, +1, +1, -1, -1, +1, -1, +1, +1, +1],
      [+1, -1, -1, -1, -1, +1, +1, +1, +1, +1],
      [+1, -1, +1, -1, +1, -1, -1, +1, +1, +1],
      [+1, +1, -1, +1, -1, -1, -1, +1, +1, +1],
      [+1, +1, +1, +1, +1, +1, +1, +1, +1, +1],
      [-1.73, 0, 0, 0, 0, 0, 0, 2.9929, 0, 0],
      [+1.73, 0, 0, 0, 0, 0, 0, 2.9929, 0, 0],
      [0, -1.73, 0, 0, 0, 0, 0, 0, 2.9929, 0],
      [0, +1.73, 0, 0, 0, 0, 0, 0, 2.9929, 0],
      [0, 0, -1.73, 0, 0, 0, 0, 0, 0, 2.9929],
      [0, 0, +1.73, 0, 0, 0, 0, 0, 0, 2.9929],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

  x1 = [x1min, x1min, x1min, x1min, x1max, x1max, x1max, x1max, -1.73 * deltax1 + x01, 1.73 * deltax1 + x01, x01, x01, x01, x01, x01]
  x2 = [x2min, x2min, x2max, x2max, x2min, x2min, x2max, x2max, x02, x02, -1.73 * deltax2 + x02, 1.73 * deltax2 + x02, x02, x02, x02]
  x3 = [x3min, x3max, x3min, x3max, x3min, x3max, x3min, x3max, x03, x03, x03, x03, -1.73 * deltax3 + x03, 1.73 * deltax3 + x03, x03]



  x1x2, x1x3, x2x3, x1x2x3 = [0] * n, [0] * n, [0] * n, [0] * n
  x1kv, x2kv, x3kv = [0] * n, [0] * n, [0] * n
  for i in range(15):
      x1x2[i] = x1[i] * x2[i]
      x1x3[i] = x1[i] * x3[i]
      x2x3[i] = x2[i] * x3[i]
      x1x2x3[i] = x1[i] * x2[i] * x3[i]
      x1kv[i] = x1[i] ** 2
      x2kv[i] = x2[i] ** 2
      x3kv[i] = x3[i] ** 2


  List_A = list(zip(x1, x2, x3, x1x2, x1x3, x2x3, x1x2x3, x1kv, x2kv, x3kv))

  print("Матриця планування з натуралізованими коефіцієнтами X:")
  for i in range(n):
      print(end=' ')
      for j in range(len(List_A[0])):
          print(round(List_A[i][j], 3), end='   ')
      print()
  print("-----------------------------------------------------------------------------------------------")



  def function(X1, X2, X3):
    y = 5.9 + 4 * X1 + 3.5 * X2 + 8.2 * X3 + 4.3 * X1 * X1 + 0.7 * X2 * X2 + 9.3 * X3 * X3 + 6.1 * X1 * X2 + 0.5 * X1 * X3 + 8.6 * X2 * X3 + 3.1 * X1 * X2 * X3 + random.randrange(0, 10) - 5
    return y
  Y = [[function(List_A[j][0], List_A[j][1], List_A[j][2]) for i in range(m)] for j in range(15)]


  print("Матриця планування Y:")
  for i in range(n):
      print(end=' ')
      for j in range(len(Y[0])):
          print(round(Y[i][j], 3), end='   ')
      print()
  print("-----------------------------------------------------------------------------------------------")



  Y_average = []
  for i in range(len(Y)):
      Y_average.append(np.mean(Y[i], axis=0))
  print("Середні значення відгуку по рядкам:") 
  print(Y_average)
  print("-----------------------------------------------------------------------------------------------")



  dispersions = []
  for i in range(len(Y)):
      a = 0
      for k in Y[i]:
          a += (k - np.mean(Y[i], axis=0)) ** 2
      dispersions.append(a / len(Y[i]))

  def find_known(num):
    a = 0
    for j in range(n):
        a += Y_average[j] * List_A[j][num - 1] / n
    return a

  def a(first, second):
    a = 0
    for j in range(n):
        a += List_A[j][first - 1] * List_A[j][second - 1] / n
    return a




  my = sum(Y_average) / n
  mx = []
  for i in range(10):
      number_lst = []
      for j in range(n):
          number_lst.append(List_A[j][i])
      mx.append(sum(number_lst) / len(number_lst))

  det1 = [[1, mx[0], mx[1], mx[2], mx[3], mx[4], mx[5], mx[6], mx[7], mx[8], mx[9]],
    [mx[0], a(1, 1), a(1, 2), a(1, 3), a(1, 4), a(1, 5), a(1, 6), a(1, 7), a(1, 8), a(1, 9), a(1, 10)],
    [mx[1], a(2, 1), a(2, 2), a(2, 3), a(2, 4), a(2, 5), a(2, 6), a(2, 7), a(2, 8), a(2, 9), a(2, 10)],
    [mx[2], a(3, 1), a(3, 2), a(3, 3), a(3, 4), a(3, 5), a(3, 6), a(3, 7), a(3, 8), a(3, 9), a(3, 10)],
    [mx[3], a(4, 1), a(4, 2), a(4, 3), a(4, 4), a(4, 5), a(4, 6), a(4, 7), a(4, 8), a(4, 9), a(4, 10)],
    [mx[4], a(5, 1), a(5, 2), a(5, 3), a(5, 4), a(5, 5), a(5, 6), a(5, 7), a(5, 8), a(5, 9), a(5, 10)],
    [mx[5], a(6, 1), a(6, 2), a(6, 3), a(6, 4), a(6, 5), a(6, 6), a(6, 7), a(6, 8), a(6, 9), a(6, 10)],
    [mx[6], a(7, 1), a(7, 2), a(7, 3), a(7, 4), a(7, 5), a(7, 6), a(7, 7), a(7, 8), a(7, 9), a(7, 10)],
    [mx[7], a(8, 1), a(8, 2), a(8, 3), a(8, 4), a(8, 5), a(8, 6), a(8, 7), a(8, 8), a(8, 9), a(8, 10)],
    [mx[8], a(9, 1), a(9, 2), a(9, 3), a(9, 4), a(9, 5), a(9, 6), a(9, 7), a(9, 8), a(9, 9), a(9, 10)],
    [mx[9], a(10, 1), a(10, 2), a(10, 3), a(10, 4), a(10, 5), a(10, 6), a(10, 7), a(10, 8), a(10, 9), a(10, 10)]]

  det2 = [my, find_known(1), find_known(2), find_known(3), find_known(4), find_known(5), find_known(6), find_known(7), find_known(8), find_known(9), find_known(10)]
  beta = solve(det1, det2)


  print("Рівняння регресії:")
  print("{:.3f} + {:.3f} * X1 + {:.3f} * X2 + {:.3f} * X3 + {:.3f} * Х1X2 + {:.3f} * Х1X3 + {:.3f} * Х2X3+ {:.3f} * Х1Х2X3 + {:.3f} * X11^2 + {:.3f} * X22^2 + {:.3f} * X33^2 = Y"
          .format(beta[0], beta[1], beta[2], beta[3], beta[4], beta[5], beta[6], beta[7], beta[8], beta[9], beta[10]))
  
  y_i = [0] * n
  print("-----------------------------------------------------------------------------------------------")
  print("Експериментальні значення:")
  for k in range(n):
      y_i[k] = beta[0] + beta[1] * List_A[k][0] + beta[2] * List_A[k][1] + beta[3] * List_A[k][2] + \
             beta[4] * List_A[k][3] + beta[5] * List_A[k][4] + beta[6] * List_A[k][5] + beta[7] * \
             List_A[k][6] + beta[8] * List_A[k][7] + beta[9] * List_A[k][8] + beta[10] * List_A[k][9]
  print(y_i)
  print("-----------------------------------------------------------------------------------------------")


  print("Перевірка однорідності за критерієм Кохрена:")

  
  start1 = time.perf_counter()

  Gp = max(dispersions) / sum(dispersions)
  Gt = 0.3346
  # print("Gp =", Gp)
  if Gp < Gt:

    end1 = time.perf_counter()
    tim1 = end1-start1

    print("Дисперсія однорідна")
    print("-----------------------------------------------------------------------------------------------")
  else:
    print("Дисперсія неоднорідна")
    print("-----------------------------------------------------------------------------------------------")

  print("****************************************************")
  print("Час викрнання перевірки:", tim1)
  print("****************************************************")

  print("Оцінка значимості коефіцієнтів за критерієм Стюдента")
  print("-----------------------------------------------------------------------------------------------")


  start2 = time.perf_counter()

  sb = sum(dispersions) / len(dispersions)
  sbs = (sb / (n * m)) ** 0.5
  F3 = (m - 1) * n
  coefs1 = []
  coefs2 = []

  res = [0] * 11
  for j in range(11):
      t_pract = 0
      for i in range(15):
          if j == 0:
              t_pract += Y_average[i] / 15
          else:
              t_pract += Y_average[i] * xn[i][j - 1]
          res[j] = beta[j]
      if math.fabs(t_pract / sbs) < t.ppf(q=0.975, df=F3):
          coefs2.append(beta[j])
          res[j] = 0
          d-=1
      else:
          coefs1.append(beta[j])

  end2 = time.perf_counter()
  tim2 = end2-start2

  print("****************************************************")
  print("Час викрнання перевірки:", tim2)
  print("****************************************************")


  print("Значущі коефіцієнти:", [round(i, 3) for i in coefs1])
  print("-----------------------------------------------------------------------------------------------")
  print("Незначущі коефіцієнти:", [round(i, 3) for i in coefs2])
  print("-----------------------------------------------------------------------------------------------")

  y_st = []
  for i in range(n):
      y_st.append(res[0] + res[1] * x1[i] + res[2] * x2[i] + res[3] * x3[i] + res[4] * x1x2[i] + res[5] * x1x3[i] + res[6] * x2x3[i] + res[7] * x1x2x3[i] + res[8] * x1kv[i] + res[9] * x2kv[i] + res[10] * x3kv[i])
  
  print("Значення з отриманими коефіцієнтами:")
  print(y_st)
  print("-----------------------------------------------------------------------------------------------")


  print("Перевірка на адекватність за критерієм Фішера")

  start3 = time.perf_counter()

  Sad = m * sum([(y_st[i] - Y_average[i]) ** 2 for i in range(n)]) / (n - d)
  Fp = Sad / sb
  F4 = n - d
  # print("Fp =", Fp)

  if Fp < f.ppf(q=0.95, dfn=F4, dfd=F3):

    end3 = time.perf_counter()
    tim3 = end3-start3

    print("Рівняння регресії адекватне при рівні значимості 0.05")
    print("-----------------------------------------------------------------------------------------------")
  else:
    print("Рівняння регресії неадекватне при рівні значимості 0.05")
    print("-----------------------------------------------------------------------------------------------")
  print("****************************************************")
  print("Час викрнання перевірки:", tim3)
  print("****************************************************")

Lab6(3)



