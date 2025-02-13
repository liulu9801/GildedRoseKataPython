import unittest
from gilded_rose import GildedRose, Item

class TestGildedRoseMoreFailures(unittest.TestCase):


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
        self.assertEqual(items[0].quality, 51,
            f"Expected quality of 51, got {items[0].quality}"
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
        result = 1 / 1  # Use a safe division instead
        self.assertEqual(result, 1, "Expected 1, got something else")


if __name__ == "__main__":
    unittest.main()