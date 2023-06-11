import json


def write_order_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r') as f_n:
        dict_to_json = json.load(f_n)

    dict_to_json['orders'].append({
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    })
    with open('orders.json', 'w', encoding='utf-8') as f_n:
        json.dump(dict_to_json, f_n, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    write_order_json('Сервер', 13, 2300, 'buyer', '12.09.23')
