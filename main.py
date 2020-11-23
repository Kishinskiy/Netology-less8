#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().splitlines()  # возвращаем список из строк файла

def get_cook_book(file_name):
    c = []  # блок для рецепта  с ингридиентами
    cook_book = {}  # итоговый словарь с рецептами
    for w in read_file('recipes.txt'):  # читаем строки из файла
        if w != '':  # пока не дошли до пустой строки наполняем список рецептами
            c.append(w)
        else:
            i = 2
            ing_list = []
            for n in range(int(c[1])):  # проходим циклом по ингредиентам
                ing = c[i].split('|')  # преобразуем строку с ингредиентами в список, разделяя по символу '|'
                ing_list.append({'ingredient_name': ing[0], 'quantity': ing[1],
                                 'measure': ing[2]})  # формируем список словарей с ингредиентами
                i += 1
            cook_book.update({c[0]: ing_list}) #добовляем получившейся список в словарь с ключем первого элемента блока
            c = [] #обмнуляем наш блок
    return cook_book

if __name__ == '__main__':


    print(get_cook_book('recipes.txt'))
