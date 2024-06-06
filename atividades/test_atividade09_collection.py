import pytest
from  python.atividades.atividade09_collection import Item, ItemCollection

def test_add_item():
    collection = ItemCollection()
    item = Item("item1")
    collection.add_item(item)
    assert item in collection.get_items()

def test_remove_item():
    collection = ItemCollection()
    item = Item("item1")
    collection.add_item(item)
    collection.remove_item(item)
    assert item not in collection.get_items()

def test_add_invalid_item():
    collection = ItemCollection()
    with pytest.raises(ValueError):
        collection.add_item("invalid_item")

def test_remove_nonexistent_item():
    collection = ItemCollection()
    item = Item("item1")
    with pytest.raises(ValueError):
        collection.remove_item(item)
