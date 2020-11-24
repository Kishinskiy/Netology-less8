#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def read_file(file_name):
    with open(file_name, 'r') as file:
        sting_list = file.read().splitlines()
        sting_list.append('') #Добавляем пустую строку в конец файла, нажно для того что бы записать в словарь все рецепты, так как функция get_cook_book разделяет блюда по пустой строке.
        return  sting_list# возвращаем список из строк файла


def get_cook_book(file_name):
    c = []  # блок для рецепта
    cook_book = {}  # итоговый словарь с рецептами
    for w in read_file(file_name):  # читаем строки из файла
        if w != '':  # пока не дошли до пустой строки наполняем список рецептами
            c.append(w)
        else:
            i = 2
            ing_list = []
            for n in range(int(c[1])):  # проходим циклом по ингредиентам
                # преобразуем строку с ингредиентами в список, разделяя по
                # символу '|'
                ing = c[i].split('|')
                ing_list.append({'ingredient_name': ing[0], 'quantity': ing[1],
                                 'measure': ing[2]})  # формируем список словарей с ингредиентами
                i += 1
            # добовляем получившейся список в словарь с ключем первого элемента
            # блока
            cook_book.update({c[0]: ing_list})
            c = []  # обмнуляем наш блок
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):

    cook_book = get_cook_book('recipes.txt')

    shop_list = {}
    for d in dishes:
        for s in cook_book[d]:
            ingr = s['ingredient_name']
            meas = s['measure']
            quant = s['quantity']

            shop_list.update(
                {ingr: {'measure': meas, 'quanitiy': int(quant) * person_count}})

    return shop_list


if __name__ == '__main__':

    print(get_cook_book('recipes.txt'))

    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
