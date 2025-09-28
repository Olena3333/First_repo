#ВИЗНАЧЕННЯ ФУНКЦІЇ
def greeting():
    print("Hello world!")
greeting()

####################################
def print_max(a: int, b: int):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')

print_max(3, 4)  # пряма передача значень

x = 5
y = 7
print_max(x, y)  # передача змінних у якості аргументів
####################################


#ФУНКЦІЯ ІЗ ПАРАМЕТРАМИ
def invite_to_event(username):
    return f"Dear {username}, we have the honour to invite you to our event"
print(invite_to_event("Tim"))

#######Задача на функцію
def string_to_codes(string: str) -> dict:
    # Ініціалізація словника для зберігання кодів
    codes = {}  
    # Перебір кожного символу в рядку
    for ch in string:  
        # Перевірка, чи символ вже є в словнику
        if ch not in codes:
            # Додавання пари символ-код в словник  
            codes[ch] = ord(ch)  
    return codes

result = string_to_codes("Hello world!")
print(result)
#######ЗНАЧЕННЯ ЗА ЗАМОВЧУВАННЯМ
def get_fullname(first_name, last_name, middle_name=""):
    if middle_name:
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}"
    
#########+КЛЮЧОВІ (ІМЕНОВАНІ) АРГУМЕНТИ
def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        spaces = (length - len(string)) // 2
        return " " * spaces + string
    #############ЗМІННА КІЛЬКІСТЬ ПАРАМЕТРІВ
    def first(size, *args):
        return size+len(args)
    def second(size, **kwargs):
        return size+len(kwargs)