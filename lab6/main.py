import numpy as np
import random as rnd

MIN_DISTANCE = 1
MAX_DISTANCE = 10

def fill_matr(n):
    matr = np.zeros((n, n), dtype = float)
    for i in range(n):
        for j in range(i+1, n):
            t = rnd.randint(MIN_DISTANCE, MAX_DISTANCE)
            matr[i][j], matr[j][i] = t, t
    return m


m = 5  # количество муравьев и городов
e = 2  # количество элитных муравьев

alpha = 2    # коэффициент влияния пути
betta = 1  # коэффициент влияния феромона
Q = MIN_DISTANCE * m  # коэффициент предполагаемого наилучшего пути
t_max = 200   # максимальное число муравьев
ro = 0.5  # коэффициент испарения


def best_way(m, e, matr, t_max, alpha, beta, ro, q):
    nue = 1 / matr  # количество феромонов на ребре
    
    teta = np.random.sample((m, m))  # расстояние между городами
    T_min = None  # min path
    L_min = None  # min len of path 

    t = 0  # первый муравей

    while t < t_max:
        teta_k = np.zeros((m, m)) #количество феромонов на путях

        for k in range(m):  # для каждого муравья в текущем городе
            Tk = [k] # города которые прошел муравей
            Lk = 0 # длина этого маршрута
            i = k   # текущий город

            while len(Tk) != m:
                J = [r for r in range(m)]   # генерируются все возможные города
                for c in Tk:  # удаляются посещенные города
                    J.remove(c)

                P = [0 for a in J]  # вероятность, что муравей выберет конкретный город

                for j in J:
                    # вычисляется вероятность перехода во все города
                    if matr[i][j] != 0:  # если путь существует
                        buf = sum((teta[i][l] ** alpha) * (nue[i][l] ** beta) for l in J)
                        P[J.index(j)] = (teta[i][j] ** alpha) * (nue[i][j] ** beta) / buf
                    else:
                        P[J.index(j)] = 0

                Pmax = max(P)
                if Pmax == 0:
                    break

                index = P.index(Pmax)  # индекс выбранного города
                Tk.append(J[index])   # добавим город в список посещенных городов
                Lk += matr[i][J[index]]  # добавляем длину 
                i = J.pop(index)  # переходим в следующий город

            if L_min is None or (Lk + matr[Tk[0]][Tk[-1]]) < L_min:  # проверка того что это не минимум
                L_min = Lk + matr[Tk[0]][Tk[-1]]                   # !не забыть про дорогу домой 
                T_min = Tk

            for g in range(len(Tk) - 1):   # обновляем феромоны на путях
                a = Tk[g]
                b = Tk[g + 1]
                teta_k[a][b] += q / Lk

        teta_e = (e * q / L_min) if L_min else 0   # количество откладываемого феромона
        teta = (1 - ro) * teta + teta_k + teta_e     # обновляем феромоны после смены муравья
        t += 1

    return T_min, L_min


if __name__ == "__main__":
   # D = fill_dis_matr(m)  # matrix of distance
    # d_fix = np.array([[0, 5, 7, 10, 5],
    #                   [5, 0, 6, 2, 8],
    #                   [7, 6, 0, 8, 8],
    #                   [10, 2, 8, 0, 6],
    #                   [5, 8, 8, 6, 0]])
    d_fix = np.array([[0,   6,   3,   7,   1],
             [6,   0,   8,  10,   6],
             [3,   8,   0,   6,   7],
             [7,  10,   6,   0,   5],
             [1,   6,   7,   5,   0]])

    print(best_way(m, e,d_fix, t_max, alpha, betta, ro, Q))