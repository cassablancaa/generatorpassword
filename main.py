import random
import string
from functools import wraps

# Dekorator do logowania
def log_generation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Wygenerowano hasło: {result}")
        return result
    return wrapper

# Deskryptor do zarządzania hasłem
class PasswordDescriptor:
    def __get__(self, instance, owner):
        return instance._password

    def __set__(self, instance, value):
        if not isinstance(value, str) or len(value) < 8:
            raise ValueError("Hasło musi mieć co najmniej 8 znaków.")
        instance._password = value

# Metaklasa do dodania dodatkowych atrybutów
class PasswordMeta(type):
    def __new__(cls, name, bases, dct):
        dct['generated_count'] = 0  # Dodajemy licznik wygenerowanych haseł
        return super().__new__(cls, name, bases, dct)

# Klasa główna z wykorzystaniem metaklasy
class PasswordGenerator(metaclass=PasswordMeta):
    password = PasswordDescriptor()  # Deskryptor do zarządzania hasłem

    def __init__(self, length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True):
        if not isinstance(length, int):
            raise TypeError("Długość hasła musi być liczbą całkowitą.")
        if length < 8:
            raise ValueError("Hasło musi mieć co najmniej 8 znaków.")
        if length > 26:  # Maksymalna długość hasła to teraz 26
            raise ValueError("Hasło nie może być dłuższe niż 26 znaków.")
        self.length = length
        self.use_lowercase = use_lowercase
        self.use_uppercase = use_uppercase
        self.use_digits = use_digits
        self.use_special_chars = use_special_chars
        self._password = None

    @log_generation
    def generate_password(self):
        characters = []
        if self.use_lowercase:
            characters.extend(string.ascii_lowercase)  # Dodaj małe litery
        if self.use_uppercase:
            characters.extend(string.ascii_uppercase)  # Dodaj duże litery
        if self.use_digits:
            characters.extend(string.digits)  # Dodaj cyfry
        if self.use_special_chars:
            characters.extend(string.punctuation)  # Dodaj znaki specjalne

        if not characters:
            raise ValueError("Musisz wybrać przynajmniej jeden rodzaj znaków.")

        self._password = ''.join(random.choice(characters) for _ in range(self.length))
        self.__class__.generated_count += 1  # Zwiększ licznik haseł
        return self._password

    @classmethod
    def get_generated_count(cls):
        return cls.generated_count

# Funkcja do pobierania danych od użytkownika
def get_user_input():
    print("Witaj w generatorze haseł!")
    length = int(input("Podaj długość hasła (8-26): "))
    use_lowercase = input("Czy używać małych liter? (t/n): ").lower() == 't'
    use_uppercase = input("Czy używać dużych liter? (t/n): ").lower() == 't'
    use_digits = input("Czy używać cyfr? (t/n): ").lower() == 't'
    use_special_chars = input("Czy używać znaków specjalnych? (t/n): ").lower() == 't'
    return length, use_lowercase, use_uppercase, use_digits, use_special_chars

# Funkcja do zapisywania hasła do pliku
def save_password_to_file(password, filename="passwords.txt"):
    with open(filename, "a") as file:
        file.write(password + "\n")
    print(f"Hasło zostało zapisane do pliku '{filename}'.")

# Główna funkcja programu
def main():
    try:
        # Pobierz dane od użytkownika
        length, use_lowercase, use_uppercase, use_digits, use_special_chars = get_user_input()

        # Utwórz obiekt generatora haseł
        generator = PasswordGenerator(length, use_lowercase, use_uppercase, use_digits, use_special_chars)

        # Wygeneruj hasło
        password = generator.generate_password()
        print(f"Wygenerowane hasło: {password}")

        # Zapisz hasło do pliku, jeśli użytkownik chce
        save_to_file = input("Czy zapisać hasło do pliku? (t/n): ").lower() == 't'
        if save_to_file:
            save_password_to_file(password)

        # Wyświetl liczbę wygenerowanych haseł
        print(f"Liczba wygenerowanych haseł: {PasswordGenerator.get_generated_count()}")

    except ValueError as e:
        print(f"Błąd: {e}")
    except TypeError as e:
        print(f"Błąd: {e}")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")

if __name__ == "__main__":
    main()