import json
from unittest import TestCase, main
from working_with_files.csv_training import task_13
from working_with_files.json_training import is_correct_json


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


if __name__ == "__main__":  # for debugging of tests themselves
    main()
