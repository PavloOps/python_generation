from unittest import TestCase, main
from working_with_files.csv_training import task_13


class CsvTask13Test(TestCase):
    def test_csv_task3(self):
        self.assertEqual(
            task_13(
                r"C:\Users\Olya\PycharmProjects\learning_Python_generation\working_with_files\prices.csv"),
            "Вареники: Дикси")

    # here should be negative tests


if __name__ == "__main__":  # for debugging of tests themselves
    main()
