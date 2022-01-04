import unittest

import pandas as pd

from app.transformer import join


class TestTransformer(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.users = pd.DataFrame(
            [
                {
                    "user_id": 0,
                    "email": "john.doe@devskiller.com",
                },
                {
                    "user_id": 1,
                    "email": "alice.doe@devskiller.com",
                },
            ]
        ).set_index("user_id")
        cls.orders = pd.DataFrame(
            [
                {
                    "order_id": 0,
                    "user_id": 0,
                    "item": "Bananas",
                },
                {
                    "order_id": 1,
                    "user_id": 0,
                    "item": "Apples",
                },
                {
                    "order_id": 2,
                    "user_id": 1,
                    "item": "Oranges",
                },
            ]
        ).set_index("order_id")

    def test_join_results_valid_number_of_columns(self):
        result = join(self.orders, self.users)
        self.assertEqual(len(result.columns), 3)

    def test_join_results_valid_emails(self):
        result = join(self.orders, self.users)
        emails = result["email"].tolist()
        self.assertListEqual(
            emails,
            [
                "john.doe@devskiller.com",
                "john.doe@devskiller.com",
                "alice.doe@devskiller.com",
            ],
        )
