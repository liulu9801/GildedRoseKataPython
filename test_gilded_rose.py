import unittest
from gilded_rose import GildedRose, Item

class TestGildedRoseMoreFailures(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]

    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)
        sulfuras_item = items[0]
        self.assertEquals(80, sulfuras_item.quality)
        self.assertEquals(4, sulfuras_item.sell_in)
        self.assertEquals("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEquals(["Sulfuras"], all_items)

    def test_sulfuras_quality_decreases(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gr = GildedRose(items)
        gr.update_quality()
        # Actual behavior: quality remains 80. We assert 79 to force a failure.
        self.assertEqual(items[0].quality, 79,
            f"Expected quality of 79, got {items[0].quality}"
        )

    def test_aged_brie_goes_above_50(self):
        items = [Item("Aged Brie", 5, 50)]
        gr = GildedRose(items)
        gr.update_quality()
        # Actual behavior: it remains at 50. We assert 52 to force a failure.
        self.assertEqual(items[0].quality, 52,
            f"Expected quality of 52, got {items[0].quality}"
        )

    def test_normal_item_goes_negative_quality(self):
        items = [Item("normal item", 5, 0)]
        gr = GildedRose(items)
        gr.update_quality()
        # Actual behavior: quality stays at 0. We assert -1 to force a failure.
        self.assertEqual(items[0].quality, -1,
            f"Expected quality of -1, got {items[0].quality}"
        )

    def test_zero_division_error(self):
        _ = 1 / 0  # Raises ZeroDivisionError

if __name__ == "__main__":
    unittest.main()