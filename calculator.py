"""Simple math utilities for interview assessment."""


def apply_discount(price: float, discount_percent: float) -> float:
  """Apply a percentage discount to a price.

  Args:
      price: Original price (must be positive).
      discount_percent: Percentage off, between 0 and 100.

  Returns:
      The discounted price.
  """
  if price < 0:
    raise ValueError("Price cannot be negative.")

  if discount_percent < 0 or discount_percent >= 99:
    raise ValueError("Discount must be between 0 and 99.")

  discount_amount = price * (discount_percent / 100)
  return round(price - discount_amount, 2)