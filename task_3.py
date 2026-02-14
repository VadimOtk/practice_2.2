import requests
import json
import os

currency_data = None
currency_groups = {}

def fetch_currency_rates():
    global currency_data
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    response.raise_for_status()
    currency_data = response.json()

def show_all_currencies():
    for code, info in currency_data['Valute'].items():
        print(f"{code}: {info['Name']} = {info['Value']} ₽ за {info['Nominal']}")

def show_currency_by_code(code):
    info = currency_data['Valute'].get(code)
    if info:
        print(f"{code}: {info['Name']} = {info['Value']} ₽ за {info['Nominal']}")
    else:
        print("Валюта не найдена")

def create_group(group_name):
    if group_name in currency_groups:
        print("Группа уже существует")
        return
    currency_groups[group_name] = []
    print("Группа создана")

def show_all_groups():
    if not currency_groups:
        print("Нет созданных групп")
        return
    for name, currencies in currency_groups.items():
        print(f"{name}: {', '.join(currencies) if currencies else 'пусто'}")

def add_currency_to_group(group_name, currency_code):
    currency_code = currency_code
    if group_name not in currency_groups:
        print("Группа не найдена")
        return
    if currency_code in currency_groups[group_name]:
        print("Валюта уже в группе")
        return
    currency_groups[group_name].append(currency_code)
    print("Валюта добавлена в группу")

def remove_currency_from_group(group_name, currency_code):
    currency_code = currency_code
    if group_name not in currency_groups:
        print("Группа не найдена")
        return
    if currency_code not in currency_groups[group_name]:
        print("Валюта не найдена в группе")
        return
    currency_groups[group_name].remove(currency_code)
    print("Валюта удалена из группы")

def save_groups():
    with open('resource/save.json', 'w', encoding='utf-8') as f:
        json.dump(currency_groups, f)
    print("Группы сохранены")

def load_groups():
    global currency_groups
    if os.path.exists('resource/save.json'):
        with open('resource/save.json', 'r', encoding='utf-8') as f:
            currency_groups = json.load(f)
        print("Группы загружены")
    else:
        currency_groups = {}
        print("Файл сохранения не найден, созданы пустые группы")

def main():
    load_groups()
    fetch_currency_rates()

    while True:
        print("\n1. Показать все валюты")
        print("2. Показать валюту по коду")
        print("3. Создать группу")
        print("4. Показать все группы")
        print("5. Добавить валюту в группу")
        print("6. Удалить валюту из группы")
        print("7. Сохранить группы")
        print("8. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            show_all_currencies()

        elif choice == '2':
            code = input("Введите код валюты: ")
            show_currency_by_code(code)

        elif choice == '3':
            name = input("Введите название группы: ")
            create_group(name)

        elif choice == '4':
            show_all_groups()

        elif choice == '5':
            group = input("Название группы: ")
            code = input("Код валюты: ")
            add_currency_to_group(group, code)

        elif choice == '6':
            group = input("Название группы: ")
            code = input("Код валюты: ")
            remove_currency_from_group(group, code)

        elif choice == '7':
            save_groups()

        elif choice == '8':
            save_groups()
            break

        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()