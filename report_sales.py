class Report:
    def __init__(self, lst, min_price=0):
        self.lst = lst
        self.min_price = min_price


    def total_revenue(self):
        total = 0
        for dict1 in self.lst:
            total += dict1['price'] * dict1['quantity']
        print(f"Общая выручка: {total}")


    def items_by_category(self):
        dict_items = dict()
        for dict1 in self.lst:
            k = dict1['category']
            v = dict1['item']
            if k not in dict_items:
                dict_items[k] = [v]
            else:
                if v not in dict_items[k]:
                    dict_items[k].append(v)
        print(f"Товары по категориям: {dict_items}")


    def expensive_purchases(self):
        output_list=[]
        for dict1 in self.lst:
            if dict1['price'] >= self.min_price:
                output_list.append(dict1)
        print(f"Покупки дороже {self.min_price}: {output_list}")


    def average_price_by_category(self):
        dict_result = dict()
        for dict1 in self.lst:
            k = dict1['category']
            v = dict1['price']
            if k not in dict_result:
                dict_result[k] = [v]
            else:
                if v not in dict_result[k]:
                    dict_result[k].append(v)
        dict_result = {k:sum(v)/len(v) for k, v in dict_result.items()}
        print(f"Средняя цена по категориям: {dict_result}")


    def most_frequent_category(self):
        dict_result=dict()
        for dict1 in self.lst:
            k = dict1['category']
            v = dict1['quantity']
            if k not in dict_result:
                dict_result[k] = [v]
            else:
                if v not in dict_result[k]:
                    dict_result[k].append(v)
        dict_result = {k:sum(v) for k, v in dict_result.items()}
        print(f"Категория с наибольшим количеством проданных товаров: {max(dict_result, key=dict_result.get)}")


purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]
report = Report(purchases, 1.0)
report.total_revenue()
report.items_by_category()
report.expensive_purchases()
report.average_price_by_category()
