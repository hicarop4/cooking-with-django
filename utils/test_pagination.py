from unittest import TestCase
from utils.pagination import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=1
        )['pagination']

        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=1
        )['pagination']

        self.assertEqual([1, 2, 3, 4], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=2
        )['pagination']

        self.assertEqual([1, 2, 3, 4], pagination)

    def test_make_sure_middle_ranges_are_correct(self):
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=3
        )['pagination']

        self.assertEqual([2, 3, 4, 5], pagination)

        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=4
        )['pagination']

        self.assertEqual([3, 4, 5, 6], pagination)

        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=5
        )['pagination']

        self.assertEqual([4, 5, 6, 7], pagination)

        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=6
        )['pagination']

        self.assertEqual([5, 6, 7, 8], pagination)

    def test_make_pagination_range_is_static_when_last_page_is_next(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=28
        )['pagination']

        self.assertEqual([17, 18, 19, 20], pagination)