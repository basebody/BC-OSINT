import csv
import os
import sys
from datetime import date
from colorama import *

# Инициализация colorama
init(autoreset=True)

# Выводит, если значение есть
def print_if_exists(label, value): 
    if value and value.strip() != '':
        print(f"{label}: {value}")


# Очистка экрана
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Загрузка данных из CSV
def load_csv(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print(Fore.RED + f"Файл {filename} не знайдено.")
        sys.exit(1)


ascii_art = """
█████╗  ██████╗      ██████╗ ███████╗██╗███╗   ██╗████████╗
██╔══██╗██╔════╝    ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
██████╔╝██║         ██║   ██║███████╗██║██╔██╗ ██║   ██║
██╔══██╗██║         ██║   ██║╚════██║██║██║╚██╗██║   ██║
██████╔╝╚██████╗    ╚██████╔╝███████║██║██║ ╚████║   ██║
╚═════╝  ╚═════╝     ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝
""".strip().split('\n')

# Оттенки от тёмно-красного к ярко-красному (можно расширить)
red_shades = [52, 88, 124, 160, 196, 203, 210]

def print_ascii_with_gradient(lines):
    total_lines = len(lines)
    max_steps = len(red_shades)
    step = max_steps / total_lines

    for i, line in enumerate(lines):
        color_index = red_shades[min(int(i * step), max_steps - 1)]
        print(f'\033[38;5;{color_index}m{line}{Style.RESET_ALL}')

def show_menu():
    print(Fore.RED + "\nОберіть дію:")
    print(Fore.RED + "1. Показати всі записи")
    print(Fore.RED + "2. Пошук за іменем")
    print(Fore.RED + "3. Пошук за школою")
    print(Fore.RED + "4. Пошук за номером телефону")
    print(Fore.RED + "5. Пошук за ПІБ (Прізвище Ім’я По батькові)")
    print(Fore.RED + "6. Пошук за посиланням на TikTok")
    print(Fore.RED + "7. Вихід")

# Печать полной информации о человеке
def print_full_info(row):
    print("-" * 40)
    print_if_exists(Fore.LIGHTRED_EX + "[+] " + "ID", row['ID'])
    print(Fore.LIGHTRED_EX + "[+] " + f"ПІБ: {row['Прізвище']} {row['Ім\'я']} {row['По-батькові'] if row['По-батькові'] != "" else ''}")
    print_if_exists(Fore.LIGHTRED_EX + "[+] " + "День народження", row['Дата народження'])
    print(Fore.LIGHTRED_EX + "[+] " + f"Рік народження: {date.today().year - int(''.join(filter(str.isdigit, row["Клас"]))) - 6 if row['Клас'] != "" else ''}")
    print_if_exists(Fore.LIGHTRED_EX + "[+] " + "Телефон", row['Номер телефону'])
    print_if_exists(Fore.LIGHTRED_EX + "[+] " + "Місто", row['Місто'])
    print_if_exists(Fore.LIGHTRED_EX + "[+] " + "Адреса", row['Адресса'])
    # print_if_exists("Телеграм юзернейм", row['Телеграм'])
    print_if_exists(Fore.LIGHTRED_EX + "[+] " + "Тікток аккаунт", row['Тікток'])
    # print_if_exists("Супруг/Супруга", row['Супруг'])
    print_if_exists(Fore.LIGHTRED_EX + "[+] " + "ПІБ мами", row['Мати'])
    print_if_exists(Fore.LIGHTRED_EX + "[+] " + "Телефон мами", row['Телефон мати'])
    # print_if_exists("Дата народження мами", row['Дата народження мами'])
    print_if_exists(Fore.LIGHTRED_EX + "[+] " + "ПІБ батька", row['Батько'])
    print_if_exists(Fore.LIGHTRED_EX + "[+] " + "Телефон батька", row['Телефон батька'])
    # print_if_exists("Дата народження батька", row['Дата народження батька'])
    print_if_exists(Fore.LIGHTRED_EX + "[+] " + "Статус", row['Статус'])
    print_if_exists(Fore.LIGHTRED_EX + "[+] " + "Предмети", row['Предмети'])
    print_if_exists(Fore.LIGHTRED_EX + "[+] " + "Місце навчання", row['Школа'])
    print_if_exists(Fore.LIGHTRED_EX + "[+] " + "Клас", row['Клас'])
    # print_if_exists("Лице", row['Лице'])
    # print_if_exists("Стаття DoxBin", row['Стаття doxbin'])
    print("-" * 40 + "\n")

# Обработка выбора
def search_by_key(data, key, value):
    results = [row for row in data if value.lower() in row[key].lower()]
    if results:
        print(Fore.GREEN + f"Знайдено {len(results)} результат(ів):")
        for row in results:
            print_full_info(row)
    else:
        print(Fore.YELLOW + "Нічого не знайдено.")

def main():
    clear()
    print_ascii_with_gradient(ascii_art)
    print(Fore.CYAN + "Завантаження даних з CSV...")
    data = load_csv('data.csv')
    
    while True:
        clear()
        print_ascii_with_gradient(ascii_art)
        show_menu()
        choice = input(Fore.LIGHTRED_EX + "Введіть номер опції: ")

        if choice == '1':
            for row in data:
                print_full_info(row)

        elif choice == '2':
            name = input("Введіть ім’я для пошуку: ")
            search_by_key(data, 'Ім\'я', name)

        elif choice == '3':
            school = input("Введіть назву школи: ")
            search_by_key(data, 'Школа', school)

        elif choice == '4':
            phone = input("Введіть номер телефону: ")
            search_by_key(data, 'Номер телефону', phone)

        elif choice == '5':
            surname = input("Прізвище: ")
            name = input("Ім’я: ")
            father = input("По батькові (або залиште порожнім): ")
            results = [
                row for row in data
                if surname.lower() in row['Прізвище'].lower()
                and name.lower() in row['Ім\'я'].lower()
                and (father.lower() in row['По-батькові'].lower() if father else True)
            ]
            if results:
                print(Fore.GREEN + f"Знайдено {len(results)} результат(ів):")
                for row in results:
                    print_full_info(row)
            else:
                print(Fore.YELLOW + "Нічого не знайдено.")

        elif choice == '6':
            tiktok = input("Введіть частину посилання на TikTok: ")
            search_by_key(data, 'Тікток', tiktok)

        elif choice == '7':
            print("До побачення!")
            break

        else:
            print(Fore.RED + "Невірний вибір. Спробуйте ще раз.")

        input(Fore.LIGHTRED_EX + "\nНатисніть Enter для продовження...")

if __name__ == '__main__':
    main()