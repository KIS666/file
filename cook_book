from pprint import pprint
def file():
    book_open = open('cook_book.txt', 'r')
    book_read = book_open.read()
    text_book = book_read.split('\n\n')
    
    list_book = []
    for food in text_book:
        list_book.append(food.split('\n'))

    name=[]
    ingred = []
    for el_book in list_book:
        ing = []
        name.append(el_book[0])
        for j in range(len(el_book)):
            if j>1:
                ing.append(el_book[j])
        ingred.append(ing)

    cook_book = dict(zip(name,ingred))

    for i in cook_book:
        list_1 = []
        for str_1 in cook_book[i]:
            list_1.append(str_1.split('|')) 
            list_inside = []
            dict_inside = dict()
            for k in list_1:
                dict_inside['ingredient_name'] = k[0]
                dict_inside['quantity'] = k[1]
                dict_inside['measure'] = k[2]
                list_inside.append(dict_inside)
                dict_inside=dict()     
        cook_book[i] = list_inside


    def get_shop_list_by_dishes(dishes, person_count):
        ingred_for_person = dict()
        for food in dishes:
            for element1 in cook_book.keys():
                if food == element1:
                    for element2 in cook_book[element1]:
                        kolvo_ingredint = dict()
                        kolvo_ingredint['quantity'] = int(element2['quantity'])*person_count
                        kolvo_ingredint['measure'] = element2['measure']
                        name = element2['ingredient_name']
                        ingred_for_person[name] = kolvo_ingredint
        print(ingred_for_person,'\n')
    get_shop_list_by_dishes(['Омлет','Утка по-пекински'], 2)
    pprint(cook_book)  
file()
