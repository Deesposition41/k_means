from random import random
import random
import matplotlib.pyplot as plt
import numpy as np

color_mas = []
n = 100  # кол-во точек
k = 10  # кол-во кластеров


def rand_points(n):
    x = np.random.randint(-20, 100, n)
    y = np.random.randint(-20, 100, n)
    return [x, y]


x = rand_points(n)[0]  # начальные точки
y = rand_points(n)[1]


def first_show(cluster_points, x_centres, y_centres):
    for i in range(len(cluster_points[0])):
        plt.scatter(cluster_points[0][i], cluster_points[1][i], color='b')
        # точки из каждого кластера отрисовываем в случайный цвет
    plt.scatter(x_centres, y_centres, color='r')  # отрисуем центры
    plt.show()


def show(cluster_points, x_centres, y_centres):
    for i in range(len(cluster_points[0])):
        color_mas.append(random_color())
    for i in range(len(cluster_points[0])):
        plt.scatter(cluster_points[0][i], cluster_points[1][i], color=color_mas[i])
        # точки из каждого кластера отрисовываем в случайный цвет
    plt.scatter(x_centres, y_centres, color='r')  # отрисуем центры
    plt.show()


def random_color():  # функция, которая генерирует один из указанных алиасов color
    color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(1)][0]
    return color


def learning_process_with_graphics(k):
    x_centres = []
    y_centres = []
    cluster_points = []

    # Первая итерация поиска точек по кластерам
    x_centres.append(center(x, y, k)[0])  # сосчитаем начальный центр
    y_centres.append(center(x, y, k)[1])
    cluster_points.append(
        add_element_in_list_of_points(x, y, x_centres[len(x_centres) - 1], y_centres[len(y_centres) - 1], k))
    new_xy_centres = new_x_c_y_c(cluster_points[0][0], cluster_points[0][1])  # считаем новые центры
    first_show([x, y], x_centres, y_centres)  # отрисуем начальные точки по кластерам и центры

    # Вторая итерация поиска точек по кластерам
    x_centres.append(new_xy_centres[0])
    y_centres.append(new_xy_centres[1])
    cluster_points.append(
        add_element_in_list_of_points(x, y, x_centres[len(x_centres) - 1], y_centres[len(y_centres) - 1], k))

    # Цикл, производящий вычисления до совпадения кластеров x и y после первых двух итераций
    while stop_learning(cluster_points[0][0], cluster_points[1][0]) and stop_learning(cluster_points[0][1],
                                                                                      cluster_points[1][
                                                                                          1]):  # пока кластеры не начнут совпадать, продолжаем цикл
        # функция add_element_in_list_of_point возвращает список списков точек. Каждый подсписок содержит точки,принадлежащие конкретному кластеру
        new_xy_centres = new_x_c_y_c(cluster_points[1][0], cluster_points[1][1])  # считаем новые центры
        x_centres.append(new_xy_centres[0])
        y_centres.append(new_xy_centres[1])
        cluster_points.append(
            add_element_in_list_of_points(x, y, x_centres[len(x_centres) - 1], y_centres[len(y_centres) - 1], k))
        cluster_points.pop(0)
        print("x_centres = ", x_centres[len(x_centres) - 1], ",", "y_centres = ", y_centres[len(y_centres) - 1])
        print("iteration_number = ", len(x_centres))
        show(cluster_points[1], x_centres[len(x_centres) - 1], y_centres[len(y_centres) - 1])
    print("Alghoritm is end!")
    return [cluster_points[1], x_centres[len(x_centres) - 1],
            y_centres[len(y_centres) - 1]]  # метод возвращает конечные центры и список списков x и y по кластерам


def learning_process(k):
    x_centres = []
    y_centres = []
    cluster_points = []

    # Первая итерация поиска точек по кластерам
    x_centres.append(center(x, y, k)[0])  # сосчитаем начальный центр
    y_centres.append(center(x, y, k)[1])
    cluster_points.append(
        add_element_in_list_of_points(x, y, x_centres[len(x_centres) - 1], y_centres[len(y_centres) - 1], k))
    new_xy_centres = new_x_c_y_c(cluster_points[0][0], cluster_points[0][1])  # считаем новые центры

    # Вторая итерация поиска точек по кластерам
    x_centres.append(new_xy_centres[0])
    y_centres.append(new_xy_centres[1])
    cluster_points.append(
        add_element_in_list_of_points(x, y, x_centres[len(x_centres) - 1], y_centres[len(y_centres) - 1], k))

    # Цикл, производящий вычисления до совпадения кластеров x и y после первых двух итераций
    while stop_learning(cluster_points[0][0], cluster_points[1][0]) and stop_learning(cluster_points[0][1],
                                                                                      cluster_points[1][
                                                                                          1]):  # пока кластеры не начнут совпадать, продолжаем цикл
        # функция add_element_in_list_of_point возвращает список списков точек. Каждый подсписок содержит точки,принадлежащие конкретному кластеру
        new_xy_centres = new_x_c_y_c(cluster_points[1][0], cluster_points[1][1])  # считаем новые центры
        x_centres.append(new_xy_centres[0])
        y_centres.append(new_xy_centres[1])
        cluster_points.append(
            add_element_in_list_of_points(x, y, x_centres[len(x_centres) - 1], y_centres[len(y_centres) - 1], k))
        cluster_points.pop(0)
        print("x_centres = ", x_centres[len(x_centres) - 1], ",", "y_centres = ", y_centres[len(y_centres) - 1])
        print("iteration_number = ", len(x_centres))
    print("Alghoritm of search begin x_centres and y_centres is end!")
    return [cluster_points[1], x_centres[len(x_centres) - 1],
            y_centres[len(y_centres) - 1]]  # метод возвращает конечные центры и список списков x и y по кластерам


def stop_learning(cl_p1, cl_p2):  # проверяет совпадение двух списков кластеров
    stop = True
    for i in range(len(cl_p1)):
        if cl_p1[i] != cl_p2[i]:
            stop = stop and False
        else:
            stop = stop and True
    return not stop


def slice_list(seq, num):  # функция, чтобы делить список на n подсписков
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out


def add_element_in_list_of_points(x, y, x_c, y_c, k):
    x_slice = slice_list([None], k)  # массив с элементом None делим на k - частей, поскольку
    y_slice = slice_list([None], k)  # без хотя бы одного элемента нельзя создать список списков
    findKNumber = 0
    for i in range(len(x)):
        distToCentres = []  # массив расстояний до центров кластеров каждой точки
        for j in range(len(x_c)):
            distToCentres.append(dist(x[i], y[i], x_c[j], y_c[j]))
        for t in range(len(distToCentres)):
            if distToCentres[t] == min(distToCentres):
                findKNumber = t  # находим порядеовый номер кластера по минимальному расстоянию до его центра от точки
        x_slice[findKNumber].append(x[i])  # добавляем эту точку в подсписок по номеру кластера
        y_slice[findKNumber].append(y[i])
    for i in range(len(x_slice)):  # удаляем None
        for j in range(len(x_slice[i])):
            if x_slice[i][j] is None:
                x_slice[i].pop(j)
                y_slice[i].pop(j)
                break
    return [x_slice, y_slice]  # возвращаем списки списков элементов по кластерам


def new_x_c_y_c(x_slice, y_slice):
    new_x_c = []
    new_y_c = []
    count = 0
    for i in range(len(x_slice)):
        count += len(x_slice[i])

    for i in range(len(x_slice)):
        new_x_c.append(sum(x_slice[i]) / count)  # считаем новые координаты центров
        new_y_c.append(sum(y_slice[i]) / count)
    return [new_x_c, new_y_c]


def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def center(x, y, k):
    x_cntr = np.mean(x)
    y_cntr = np.mean(y)
    R = dist(x_cntr, y_cntr, x[0], y[0])
    for i in range(len(x)):
        R = max(R, dist(x_cntr, y_cntr, x[i], y[i]))
    x_c, y_c = [], []
    for i in range(k):
        x_c.append(x_cntr + R * np.cos(2 * np.pi * i / k))
        y_c.append(y_cntr + R * np.sin(2 * np.pi * i / k))
    return [x_c, y_c]


def k_optimal(x, y, x_centres, y_centres):
    k_n = 0
    j_mas = []
    d_mas = []
    for j in range(len(x_centres)):
        d = 0
        for i in range(len(x)):
            d += dist(x[i], y[i], x_centres[j], y_centres[j])
        j_mas.append(d)
    for i in range(1, len(j_mas) - 1):
        d_mas.append(abs(j_mas[i] - j_mas[i + 1]) / abs(j_mas[i - 1] - j_mas[i]))
    min_d = min(d_mas)
    for i in range(len(d_mas)):
        if d_mas[i] == min_d:
            k_n = i
    return k_n if k_n > 0 else 1


if __name__ == "__main__":
    l_p = learning_process(k)
    result = learning_process_with_graphics(k_optimal(x, y, l_p[1], l_p[2]))
    show(result[0], result[1], result[2])
    # print(k_optimal(x, y, l_p[1], l_p[2]))
