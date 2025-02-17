# Generator Losowych Haseł

## Opis Projektu

Aplikacja **Generator Losowych Haseł** to program napisany w Pythonie, który generuje bezpieczne, losowe hasła na podstawie preferencji użytkownika. Użytkownik może określić długość hasła oraz wybrać rodzaje znaków, które mają zostać użyte (małe litery, duże litery, cyfry, znaki specjalne). Projekt demonstruje wykorzystanie zaawansowanych koncepcji programowania w Pythonie, takich jak klasy, metaklasy, deskryptory i dekoratory.

## Funkcje

- Generowanie haseł o długości od 8 do 26 znaków.
- Możliwość wyboru rodzajów znaków:
  - Małe litery (`a-z`).
  - Duże litery (`A-Z`).
  - Cyfry (`0-9`).
  - Znaki specjalne (np. `!@#$%^&*`).
- Zapis wygenerowanych haseł do pliku `passwords.txt`.
- Licznik wygenerowanych haseł.

## Wymagania Systemowe

- Python 3.6 lub nowszy.
- Brak dodatkowych zależności (wszystkie moduły są wbudowane w Pythona).

## Jak uruchomić program?

1. Pobierz plik `main.py`.
2. Uruchom program za pomocą polecenia:
   ```bash
   python main.py
Postępuj zgodnie z instrukcjami wyświetlanymi na ekranie.

##  Przykład użycia

Witaj w generatorze haseł!
Podaj długość hasła (8-26): 12
Czy używać małych liter? (t/n): t
Czy używać dużych liter? (t/n): t
Czy używać cyfr? (t/n): t
Czy używać znaków specjalnych? (t/n): t
Wygenerowano hasło: aB3#xY7!zQ9@
Wygenerowane hasło: aB3#xY7!zQ9@
Czy zapisać hasło do pliku? (t/n): t
Hasło zostało zapisane do pliku 'passwords.txt'.
Liczba wygenerowanych haseł: 1
Jak uruchomić testy?
Pobierz plik test.py.

##  Uruchom testy za pomocą polecenia:


python -m unittest discover -v
lub:


python test.py -v
##  Przykładowy wynik testów

test_edge_case_max_length (test.TestPasswordGenerator) ... ok
test_edge_case_min_length (test.TestPasswordGenerator) ... ok
test_generated_count (test.TestPasswordGenerator) ... ok
test_invalid_length_type (test.TestPasswordGenerator) ... ok
test_log_generation_decorator (test.TestPasswordGenerator) ... ok
test_no_characters_selected (test.TestPasswordGenerator) ... ok
test_only_digits (test.TestPasswordGenerator) ... ok
test_only_lowercase (test.TestPasswordGenerator) ... ok
test_only_special_chars (test.TestPasswordGenerator) ... ok
test_only_uppercase (test.TestPasswordGenerator) ... ok
test_password_characters (test.TestPasswordGenerator) ... ok
test_password_descriptor (test.TestPasswordGenerator) ... ok
test_password_length (test.TestPasswordGenerator) ... ok
test_password_too_short (test.TestPasswordGenerator) ... ok
test_too_long_password (test.TestPasswordGenerator) ... ok

----------------------------------------------------------------------
Ran 15 tests in 0.005s


##  Struktura Kodu
##  Diagram Klas
+-------------------+
| PasswordGenerator |
+-------------------+
| - length          |
| - use_lowercase   |
| - use_uppercase   |
| - use_digits      |
| - use_special_chars|
| - _password       |
+-------------------+
| + generate_password() |
| + get_generated_count()|
+-------------------+
##  Główne Komponenty
Klasa PasswordGenerator:

Generuje hasła na podstawie preferencji użytkownika.

Zarządza długością hasła i rodzajami znaków.

Deskryptor PasswordDescriptor:

Sprawdza, czy hasło spełnia minimalne wymagania (co najmniej 8 znaków).

Metaklasa PasswordMeta:

Dodaje licznik wygenerowanych haseł.

Dekorator log_generation:

Loguje wygenerowane hasło w konsoli.