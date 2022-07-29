import unittest

from main import paginate


class PaginatorTestCase(unittest.TestCase):

    def test_pagination(self):

        result = paginate(
            total_pages=10,
            current_page=5,
            boundaries=0,
            around=1
        )
        self.assertEqual(result,  ['...', 4, 5, 6, '...'])

        result = paginate(
            total_pages=10,
            current_page=5,
            boundaries=0,
            around=4
        )
        self.assertEqual(result,  [1, 2, 3, 4, 5, 6, 7, 8, 9, '...'])

        result = paginate(
            total_pages=5,
            current_page=4,
            boundaries=1,
            around=0
        )
        self.assertEqual(result, [1, '...', 4, 5])

        result = paginate(
            total_pages=10,
            current_page=4,
            boundaries=2,
            around=2
        )
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, '...', 9, 10])

        # TODO solve the following test
        # result = paginate(
        #     total_pages=100000000,
        #     current_page=5,
        #     boundaries=1,
        #     around=1
        # )
        # expected = [1, 2, '...', 1499998, 1499999, 1500000, 1500001, 1500002, '...', 2999999, 3000000]
        # self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
