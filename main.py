# 4. Клас комплексне число. 
# Визначити операції: множення двох комплексних чисел (оператор “*”), 
# додавання двох комплексних чисел (оператор “+”), 
# порівняння модуля комплексного числа з дійсним числом на відношеннями «менше» «більше» (оператори “<”, “>”), 
# множення комплексного числа на дійсне число (оператор “*”).

class Complex_Num:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other): # додавання
        return Complex_Num(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other): # множення
        if isinstance(other, Complex_Num):
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
            return Complex_Num(real, imag)
        elif isinstance(other, (int, float)):
            return Complex_Num(self.real * other, self.imag * other)
        return NotImplemented

    def __lt__(self, other): # порівняння на менше
        if isinstance(other, (int, float)):
            return self.modulus() < other
        return NotImplemented

    def __gt__(self, other): # порівняння на більше
        if isinstance(other, (int, float)):
            return self.modulus() > other
        return NotImplemented

    def modulus(self): # модуль комплексного числа
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    def __str__(self):
        return f"{self.real} + {self.imag}i"


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Будь ласка, введіть коректне число.")


if __name__ == "__main__":
    while True:
        print("\nОберіть операцію:")
        print("1 - Додавання комплексних чисел")
        print("2 - Множення комплексних чисел")
        print("3 - Множення комплексного числа на дійсне")
        print("4 - Порівняння модуля комплексного числа з дійсним (менше)")
        print("5 - Порівняння модуля комплексного числа з дійсним (більше)")

        choice = input("Ваш вибір: ")

        if choice not in ["1", "2", "3", "4", "5"]:
            print("Введіть число від 1 до 5. Спробуйте ще раз.")
            continue

        real1 = get_number("Введіть дійсну частину першого числа: ")
        imag1 = get_number("Введіть уявну частину першого числа: ")
        z1 = Complex_Num(real1, imag1)

        if choice in ["1", "2"]:
            real2 = get_number("Введіть дійсну частину другого числа: ")
            imag2 = get_number("Введіть уявну частину другого числа: ")
            z2 = Complex_Num(real2, imag2)

            if choice == "1":
                print("Результат додавання:", z1 + z2)
            elif choice == "2":
                print("Результат множення:", z1 * z2)

        elif choice == "3":
            real_num = get_number("Введіть дійсне число: ")
            print("Результат множення на дійсне число:", z1 * real_num)

        elif choice == "4":
            real_num = get_number("Введіть дійсне число: ")
            print(f"Модуль комплексного числа менше {real_num}:", z1 < real_num)

        elif choice == "5":
            real_num = get_number("Введіть дійсне число: ")
            print(f"Модуль комплексного числа більше {real_num}:", z1 > real_num)
