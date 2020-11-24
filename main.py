#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_cook_book():
    with open('recipes.txt', 'r') as file_work:
        cook_book = {}
        for line in file_work:
            dish_name = line[:-1]
            counter = int(file_work.readline())
            list_of_ingridient = []
            for i in range(counter):
                temp_dict = {}
                ingridient = file_work.readline()
                ing = ingridient.split('|')
                temp_dict.update({'ingredient_name': ing[0], 'quantity': ing[1],
                                  'measure': ing[2][:-1]})
                list_of_ingridient.append(temp_dict)
            cook_book.update({dish_name: list_of_ingridient})
            file_work.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book()
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
    print(get_cook_book())
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
