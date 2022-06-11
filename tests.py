import unittest

from main import paginate


class PaginatorTestCase(unittest.TestCase):

    def test_pagination(self):
        result = paginate(
            total_pages=5,
            current_page=4,
            boundaries=1
        )
        self.assertEqual(result, [1, '...', 4, 5])

        result = paginate(
            total_pages=10,
            current_page=4,
            boundaries=2,
            around=2
        )
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, '...', 9, 10])


if __name__ == '__main__':
    unittest.main()
