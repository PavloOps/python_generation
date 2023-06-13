import json
from collections import OrderedDict
from unittest import TestCase, main
from working_with_files.csv_training import task_13
from working_with_files.json_training import is_correct_json, task15
from working_with_files import zip_training
from working_with_collections.collections_training import wins
from working_with_collections.collections_training import task2_ordered_dict
from working_with_collections.collections_training import count_occurences
from working_with_collections.collections_training import task4_counter2
from working_with_functions.inner_functions_annotations import cyclic_shift


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

    def test_zip_task4(self):
        self.assertListEqual(zip_training.task4(
            r"C:\Users\Olya\PycharmProjects\learning_Python_generation\working_with_files\workbook.zip"),
            [
                'countries.json',
                'data_sample.csv',
                'earth.jpg', 'exam.txt',
                'fipi_demo_2022.pdf',
                'homework.py', 'python.pdf',
                'readme.txt',
                'shopping_list.txt',
                'task_results.xlsx'
            ]
        )


class CollectionsTest(TestCase):

    def test_wins(self):
        result1 = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])
        result2 = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Дима', 'Артур')])
        answer1 = {'Тимур': {'Дима', 'Артур'}, 'Дима': {'Артур'}}
        answer2 = {'Артур': {'Дима', 'Тимур', 'Анри'}, 'Дима': {'Артур'}}
        self.assertEqual(result1, answer1)
        self.assertEqual(result2, answer2)

    def test_task2_ordered_dict(self):
        data = OrderedDict(key1='value1', key2='value2', key3='value3', key4='value4')
        result = task2_ordered_dict(data)
        answer = OrderedDict([('key1', 'value1'), ('key4', 'value4'), ('key2', 'value2'), ('key3', 'value3')])
        self.assertEqual(result, answer)

    def test_count_occurences(self):
        word1 = 'python'
        words1 = 'Python Conferences python training python events'
        answer1 = 3

        word2 = 'Java'
        words2 = 'Python C++ C# JavaScript Go Assembler'
        answer2 = 0

        result1 = count_occurences(word1, words1)
        result2 = count_occurences(word2, words2)

        self.assertEqual(result1, answer1)
        self.assertEqual(result2, answer2)

    def test_task4_counter2(self):
        test_stack = [
            ("Говори говори до тех пор пока горем горим", '''Слов длины 2: 1
Слов длины 4: 1
Слов длины 6: 2
Слов длины 3: 2
Слов длины 5: 2'''),
            ("abcde abcd abc ab a",
            '''Слов длины 5: 1
Слов длины 4: 1
Слов длины 3: 1
Слов длины 2: 1
Слов длины 1: 1'''),
            ("abcde abcde abcde abcde abcde abcde abcde", "Слов длины 5: 7"),
            ("банан Малина арбуз Банан Черешня черешня малина банан клубника Вишня Банан Вишня Банан арбуз арбуз Банан арбуз арбуз Черешня банан", '''Слов длины 8: 1
Слов длины 6: 2
Слов длины 7: 3
Слов длины 5: 14''')
        ]
        for data, answer in test_stack:
            result = task4_counter2(data)
            self.assertEqual(result, answer)


class AnnotationTest(TestCase):
    def test_cyclic_shift(self):
        test_pack = [
            ([1, 2, 3, 4, 5], 1, [5, 1, 2, 3, 4]),
            ([1, 2, 3, 4, 5], -2, [3, 4, 5, 1, 2]),
            ([1, 2.0, 3, 4.0, 5.5], 0, [1, 2.0, 3, 4.0, 5.5]),
        ]

        for lst, step, answer in test_pack:
            cyclic_shift(lst, step)
            self.assertEqual(lst, answer)
    # here should be negative tests


if __name__ == "__main__":  # for debugging of tests themselves
    main()
