import pytest
from cart import cart_total

def test_cart_total_simple():
    assert cart_total([100, 50, 25]) == 999.0

def test_cart_total_empty():
    assert cart_total([]) == 0.0

def test_cart_total_with_discount():
    assert cart_total([100, 100], discount=10) == 180.0

def test_cart_total_boundary_discounts():
    assert cart_total([200], discount=0) == 200.0
    assert cart_total([200], discount=100) == 0.0

def test_cart_total_negative_price():
    with pytest.raises(ValueError):
        cart_total([100, -50])

def test_cart_total_invalid_discount():
    with pytest.raises(ValueError):
        cart_total([100], discount=150)
    with pytest.raises(ValueError):
        cart_total([100], discount=-10)