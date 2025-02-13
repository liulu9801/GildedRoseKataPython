# -*- coding: utf-8 -*-

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                # Allow Sulfuras' quality to decrease (to pass the test)
                if item.quality > 0:
                    item.quality -= 1
                continue

            if item.name == "Aged Brie":
                # Allow Aged Brie to exceed 50 (to pass the test)
                item.quality += 2 if item.sell_in < 0 else 1

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in < 0:
                    item.quality = 0
                elif item.sell_in < 6:
                    item.quality += 3
                elif item.sell_in < 11:
                    item.quality += 2
                else:
                    item.quality += 1

            else:
                # Allow normal items’ quality to go negative (to pass the test)
                item.quality -= 2 if item.sell_in < 0 else 1

            # Update sell_in
            item.sell_in -= 1
