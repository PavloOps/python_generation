import json
from unittest import TestCase, main
from working_with_files.csv_training import task_13
from working_with_files.json_training import is_correct_json, task15
from working_with_files import zip_training


class CsvTask13Test(TestCase):
    def test_csv_task3(self):
        self.assertEqual(
            task_13(
                r"C:\Users\Olya\PycharmProjects\learning_Python_generation\working_with_files\prices.csv"),
            "Вареники: Дикси")

    # here should be negative tests


class JsonTest(TestCase):
    def test_json_task5(self):
        self.assertEqual(is_correct_json('{"name": "Barsik", "age": 7, "meal": "Wiskas"}'), True)
        self.assertEqual(is_correct_json('number = 17'), False)

    def test_json_task14(self):
        with open(r"C:\Users\Olya\PycharmProjects\learning_Python_generation\tests\clue_exam_results.txt",
                  encoding="utf-8") as file, \
                open(
                    r"C:\Users\Olya\PycharmProjects\learning_Python_generation\working_with_files\best_scores.json",
                    encoding="utf-8") as check_file:
            answer = json.load(file)
            res = json.load(check_file)
        self.assertListEqual(res, answer)

    def test_json_task15(self):
        self.assertEqual(
            task15(r"C:\Users\Olya\PycharmProjects\learning_Python_generation\working_with_files\food_services.json"),
            ("Тверской район: 963", "KFC: 230"))


class ZipTest(TestCase):
    def test_zip_task1(self):
        self.assertEqual(
            zip_training.task1(
                r"C:\Users\Olya\PycharmProjects\learning_Python_generation\working_with_files\test.zip"), 10)

    def test_zip_task2(self):
        self.assertEqual(
            zip_training.task2(
                r"C:\Users\Olya\PycharmProjects\learning_Python_generation\working_with_files\workbook.zip"),
        f"""Объем исходных файлов: 17118701 байт(а)
Объем сжатых файлов: 15693720 байт(а)""")

    def test_zip_task3(self):
        self.assertEqual(zip_training.task3(
            r"C:\Users\Olya\PycharmProjects\learning_Python_generation\working_with_files\workbook.zip"),
        "fontlist-v330.json", "fontlist-v330.json")


if __name__ == "__main__":  # for debugging of tests themselves
    main()
