# Your task is to add the new feature to our system so that we 
# can begin selling a new category of items. First an introduction to our 
# system:

# - All items have a SellIn value which denotes the number of days we have 
# to sell the item
# - All items have a Quality value which denotes how valuable the item is
# - At the end of each day our system lowers both values for every item

# Pretty simple, right? Well this is where it gets interesting:

# - Once the sell by date has passed, Quality degrades twice as fast
# - The Quality of an item is never negative
# - "Aged Brie" actually increases in Quality the older it gets
# - The Quality of an item is never more than 50
# - "Sulfuras", being a legendary item, never has to be sold or decreases 
# in Quality
# - "Backstage passes", like aged brie, increases in Quality as it's SellIn 
# value approaches; Quality increases by 2 when there are 10 days or less 
# and by 3 when there are 5 days or less but Quality drops to 0 after the 
# concert

# We have recently signed a supplier of conjured items. This requires an 
# update to our system:

# - "Conjured" items degrade in Quality twice as fast as normal items

# Feel free to make any changes to the UpdateQuality method and add any 
# new code as long as everything still works correctly.

# Just for clarification, an item can never have its Quality increase 
# above 50, however "Sulfuras" is a legendary item and as such its 
# Quality is 80 and it never alters.

class Item():
    name = ""
    sellIn = 0
    quality = 0

    def __init__(self, name, sellIn, quality):
        self.name = name
        self.sellIn = sellIn
        self.quality = quality

    def to_string(self):
        return 'Item { name: "%s", sellIn: %d, quality: %d }' % (self.name, self.sellIn
        , self.quality) 

class Shop():
    items = []
    def __init__(self, items=[]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # Update Quality
            if item.name != 'Aged Brie' and item.name != 'Backstage passes to a TAFKAL80ETC concert':
                if (item.quality > 0):
                    if (item.name != 'Sulfuras, Hand of Ragnaros'):
                        item.quality = item.quality - 1
            else:
                if (item.quality < 50):
                    item.quality = item.quality + 1
                    if (item.name == 'Backstage passes to a TAFKAL80ETC concert'):
                        if (item.sellIn < 11):
                            if (item.quality < 50):
                                item.quality = item.quality + 1
                        if (item.sellIn < 6):
                            if (item.quality < 50):
                                item.quality = item.quality + 1

            if (item.name != 'Sulfuras, Hand of Ragnaros'):
                item.sellIn = item.sellIn - 1


            if (item.sellIn < 0):
                if (item.name != 'Aged Brie'):
                    if (item.name != 'Backstage passes to a TAFKAL80ETC concert'):
                        if (item.quality > 0):
                            if (item.name != 'Sulfuras, Hand of Ragnaros'):
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if (item.quality < 50):
                        item.quality = item.quality + 1

        return self.items

    def print_items(self):
        for item in self.items:
            print(item.to_string())


def main():
    shop = Shop([Item('Aged Brie', 100, 100)])
    shop.update_quality()
    shop.print_items()

def test():
    test_brie()
    test_sulfuras()
    test_concert()
    
def test_brie():
     # Basic
    shop = Shop([Item('Aged Brie', 100, 100)])
    shop.update_quality()
    assert(shop.items[0].sellIn == 99)
    assert(shop.items[0].quality == 100)
    shop.update_quality()
    assert(shop.items[0].sellIn == 98)
    assert(shop.items[0].quality == 100)
    # Aged brie doesnt decrease in quality
    shop = Shop([Item('Aged Brie', 100, 100)])
    for i in range(105):
        shop.update_quality() 
        assert(shop.items[0].sellIn == 100-i-1)
        assert(shop.items[0].quality == 100)
    
    shop = Shop([Item('Aged Brie', 0, 25)])
    shop.update_quality()
    # shop.print_items()
    assert(shop.items[0].sellIn == -1)
    assert(shop.items[0].quality == 25+1+1)

def test_sulfuras():
    shop = Shop([Item('Sulfuras, Hand of Ragnaros', 100, 100)])
    shop.update_quality()
    # shop.print_items()
    assert(shop.items[0].sellIn == 100)
    assert(shop.items[0].quality == 100)

    shop = Shop([Item('Sulfuras, Hand of Ragnaros', 0, 100)])
    shop.update_quality()
    # shop.print_items()
    assert(shop.items[0].sellIn == 0)
    assert(shop.items[0].quality == 100)

    shop = Shop([Item('Sulfuras, Hand of Ragnaros', 5, 25)])
    shop.update_quality()
    # shop.print_items()
    assert(shop.items[0].sellIn == 5)
    assert(shop.items[0].quality == 25)


def test_concert():
    shop = Shop([Item('Backstage passes to a TAFKAL80ETC concert', 100, 100)])
    shop.update_quality()
    # shop.print_items()
    assert(shop.items[0].sellIn == 99)
    assert(shop.items[0].quality == 100)

    # Increase when low quality
    shop = Shop([Item('Backstage passes to a TAFKAL80ETC concert', 100, 20)])
    shop.update_quality()
    # shop.print_items()
    assert(shop.items[0].sellIn == 99)
    assert(shop.items[0].quality == 20+1)

    # Increase when it gets close to the concert
    shop = Shop([Item('Backstage passes to a TAFKAL80ETC concert', 5, 20)])
    shop.update_quality()
    # shop.print_items()
    assert(shop.items[0].sellIn == 4)
    assert(shop.items[0].quality == 20+1+1+1)

    # Increase when it gets close to the concert
    shop = Shop([Item('Backstage passes to a TAFKAL80ETC concert', 1, 20)])
    shop.update_quality()
    # shop.print_items()
    assert(shop.items[0].sellIn == 0)
    assert(shop.items[0].quality == 20+1+1+1)
    
    
main()
print("Testing...")
test()
print("SUCCESS!")