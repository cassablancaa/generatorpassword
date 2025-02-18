import unittest
import string
from main import (  # Importujemy wszystko, co jest potrzebne
    PasswordGenerator,
    PasswordDescriptor,
    PasswordMeta,  # Dodajemy import PasswordMeta
    log_generation,
)

class TestPasswordGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = PasswordGenerator()

    def test_password_length(self):
        self.generator.length = 10
        password = self.generator.generate_password()
        self.assertEqual(len(password), 10)

    def test_password_characters(self):
        self.generator.length = 12
        self.generator.use_lowercase = True
        self.generator.use_uppercase = True
        self.generator.use_digits = True
        self.generator.use_special_chars = True

        password = self.generator.generate_password()
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_only_lowercase(self):
        self.generator.length = 8
        self.generator.use_lowercase = True
        self.generator.use_uppercase = False
        self.generator.use_digits = False
        self.generator.use_special_chars = False

        password = self.generator.generate_password()
        self.assertTrue(all(c in string.ascii_lowercase for c in password))

    def test_only_uppercase(self):
        self.generator.length = 8
        self.generator.use_lowercase = False
        self.generator.use_uppercase = True
        self.generator.use_digits = False
        self.generator.use_special_chars = False

        password = self.generator.generate_password()
        self.assertTrue(all(c in string.ascii_uppercase for c in password))

    def test_only_digits(self):
        self.generator.length = 8
        self.generator.use_lowercase = False
        self.generator.use_uppercase = False
        self.generator.use_digits = True
        self.generator.use_special_chars = False

        password = self.generator.generate_password()
        self.assertTrue(all(c in string.digits for c in password))

    def test_only_special_chars(self):
        self.generator.length = 8
        self.generator.use_lowercase = False
        self.generator.use_uppercase = False
        self.generator.use_digits = False
        self.generator.use_special_chars = True

        password = self.generator.generate_password()
        self.assertTrue(all(c in string.punctuation for c in password))

    def test_no_characters_selected(self):
        self.generator.use_lowercase = False
        self.generator.use_uppercase = False
        self.generator.use_digits = False
        self.generator.use_special_chars = False

        with self.assertRaises(ValueError):
            self.generator.generate_password()

    def test_password_too_short(self):
        self.generator.length = 5
        with self.assertRaises(ValueError):
            self.generator.password = "abc"

    def test_password_descriptor(self):
        class TestUser:
            password = PasswordDescriptor()

        user = TestUser()
        user.password = "ValidPassword123"
        self.assertEqual(user.password, "ValidPassword123")

        with self.assertRaises(ValueError):
            user.password = "short"

    def test_log_generation_decorator(self):
        @log_generation
        def dummy_generator():
            return "TestPassword123"

        self.assertEqual(dummy_generator(), "TestPassword123")

    def test_generated_count(self):
        initial_count = PasswordGenerator.get_generated_count()
        self.generator.generate_password()
        self.assertEqual(PasswordGenerator.get_generated_count(), initial_count + 1)

    def test_edge_case_min_length(self):
        self.generator.length = 8
        password = self.generator.generate_password()
        self.assertEqual(len(password), 8)

    def test_edge_case_max_length(self):
        self.generator.length = 26  # Maksymalna długość to teraz 26
        password = self.generator.generate_password()
        self.assertEqual(len(password), 26)

    def test_invalid_length_type(self):
        with self.assertRaises(TypeError):
            PasswordGenerator(length="invalid")

    def test_too_long_password(self):
        with self.assertRaises(ValueError):
            PasswordGenerator(length=27)  # Powinien zgłosić błąd, bo maksymalna długość to 26

if __name__ == "__main__":
    unittest.main(exit=False)