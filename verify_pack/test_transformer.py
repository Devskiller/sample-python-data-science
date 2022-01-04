import math
import unittest

import pandas as pd

from app.transformer import join


class VerifyTestTransformer(unittest.TestCase):
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
                {
                    "user_id": 2,
                    "email": "mark.doe@devskiller.com",
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
                {
                    "order_id": 3,
                    "user_id": 2,
                    "item": "Pumpkins",
                },
                {
                    "order_id": 4,
                    "user_id": 3,
                    "item": "Antimatter",
                },
            ]
        ).set_index("order_id")

    def test_join_results_valid_number_of_rows(self):
        result = join(self.orders, self.users)
        self.assertEqual(len(result.index), 5)

    def test_join_results_has_valid_index(self):
        result = join(self.orders, self.users)
        self.assertEqual(result.index.name, "order_id")
        indices = result.index.tolist()
        self.assertListEqual(indices, list(range(5)))

    def test_join_appends_nan_on_missing_user(self):
        result = join(self.orders, self.users)
        self.assertTrue(result["email"].isna().any())
