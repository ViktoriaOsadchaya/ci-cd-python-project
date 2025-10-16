import pytest
import sys
import os
from unittest.mock import patch, MagicMock

# Добавляем путь к src для импорта
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from random_generator import RandomNumberGenerator


class TestRandomNumberGenerator:
    def test_generate_random_numbers(self):
        """Тест генерации случайных чисел"""
        generator = RandomNumberGenerator.__new__(RandomNumberGenerator)

        # Тестируем генерацию чисел
        numbers = generator.generate_random_numbers(7)

        # Проверяем что получили 7 чисел
        assert len(numbers) == 7

        # Проверяем что все числа в диапазоне 1-100
        for num in numbers:
            assert 1 <= num <= 100
            assert isinstance(num, int)

    def test_generate_random_numbers_different_count(self):
        """Тест генерации разного количества чисел"""
        generator = RandomNumberGenerator.__new__(RandomNumberGenerator)

        for count in [1, 5, 10]:
            numbers = generator.generate_random_numbers(count)
            assert len(numbers) == count

    @patch('random.randint')
    def test_generate_random_numbers_with_mock(self, mock_randint):
        """Тест генерации с моком для предсказуемых результатов"""
        generator = RandomNumberGenerator.__new__(RandomNumberGenerator)
        mock_randint.return_value = 42

        numbers = generator.generate_random_numbers(3)

        # Проверяем что все числа равны 42 (значение мока)
        assert numbers == [42, 42, 42]
        assert mock_randint.call_count == 3

    def test_format_numbers(self):
        """Тест форматирования чисел для отображения"""
        generator = RandomNumberGenerator.__new__(RandomNumberGenerator)

        test_numbers = [10, 20, 30]
        formatted = generator.format_numbers(test_numbers)

        expected = "Число 1: 10\nЧисло 2: 20\nЧисло 3: 30"
        assert formatted == expected

    def test_format_numbers_empty(self):
        """Тест форматирования пустого списка"""
        generator = RandomNumberGenerator.__new__(RandomNumberGenerator)

        formatted = generator.format_numbers([])
        assert formatted == ""

    def test_format_numbers_single(self):
        """Тест форматирования одного числа"""
        generator = RandomNumberGenerator.__new__(RandomNumberGenerator)

        formatted = generator.format_numbers([99])
        assert formatted == "Число 1: 99"