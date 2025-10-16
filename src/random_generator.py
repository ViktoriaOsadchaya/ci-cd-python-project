import tkinter as tk
from tkinter import ttk, messagebox
import random
from typing import List


class RandomNumberGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор случайных чисел")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        """Создание элементов интерфейса"""
        # Заголовок
        title_label = ttk.Label(
            self.root,
            text="Генератор 7 случайных чисел",
            font=("Arial", 14, "bold")
        )
        title_label.pack(pady=10)

        # Кнопка генерации
        self.generate_button = ttk.Button(
            self.root,
            text="Сгенерировать числа",
            command=self.generate_numbers
        )
        self.generate_button.pack(pady=5)

        # Текстовое поле для отображения чисел
        self.text_display = tk.Text(
            self.root,
            height=10,
            width=30,
            font=("Courier New", 12),
            state="disabled",  # Делаем поле неизменяемым
            bg="#f0f0f0"
        )
        self.text_display.pack(pady=10, padx=20, fill="both", expand=True)

        # Полоса прокрутки для текстового поля
        scrollbar = ttk.Scrollbar(self.text_display)
        scrollbar.pack(side="right", fill="y")
        self.text_display.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text_display.yview)

    def generate_random_numbers(self, count: int = 7) -> List[int]:
        """
        Генерирует список случайных чисел

        Args:
            count: количество чисел для генерации

        Returns:
            List[int]: список случайных чисел от 1 до 100
        """
        return [random.randint(1, 100) for _ in range(count)]

    def format_numbers(self, numbers: List[int]) -> str:
        """
        Форматирует числа для отображения

        Args:
            numbers: список чисел

        Returns:
            str: отформатированная строка с числами
        """
        return "\n".join([f"Число {i + 1}: {num}" for i, num in enumerate(numbers)])

    def generate_numbers(self):
        """Основная функция генерации и отображения чисел"""
        try:
            # Генерируем 7 случайных чисел
            numbers = self.generate_random_numbers(7)

            # Форматируем для отображения
            formatted_text = self.format_numbers(numbers)

            # Обновляем текстовое поле
            self.text_display.config(state="normal")  # Временно включаем редактирование
            self.text_display.delete(1.0, tk.END)  # Очищаем поле
            self.text_display.insert(1.0, formatted_text)  # Вставляем новые числа
            self.text_display.config(state="disabled")  # Снова делаем неизменяемым

        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")


def main():
    """Запуск приложения"""
    root = tk.Tk()
    app = RandomNumberGenerator(root)
    root.mainloop()


if __name__ == "__main__":
    main()