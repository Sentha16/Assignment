#!/usr/bin/env python
# coding: utf-8

# In[21]:


import random
from datetime import datetime, timedelta

# E-Commerce Search Aggregator
def search_products(name, color, price_range, size):
    # Mock product search results
    products = [
        {"name": "Floral Skirt", "color": "Red", "price": 35, "size": "S", "in_stock": True},
        {"name": "Floral Skirt", "color": "Blue", "price": 45, "size": "S", "in_stock": False},
        {"name": "White Sneakers", "color": "White", "price": 65, "size": "8", "in_stock": True},
        {"name": "Casual Denim Jacket", "color": "Blue", "price": 80, "size": "M", "in_stock": True},
    ]
    return [product for product in products if product["name"].lower() == name.lower() and
            product["color"].lower() == color.lower() and
            product["price"] >= price_range[0] and product["price"] <= price_range[1] and
            product["size"].lower() == size.lower()]

# Shipping Time Estimator
def estimate_shipping(location, desired_date):
    # Mock shipping estimation
    today = datetime.now()
    estimated_delivery = today + timedelta(days=random.randint(1, 7))
    cost = random.uniform(5, 15)
    feasible = estimated_delivery <= desired_date
    return {"feasible": feasible, "cost": cost, "estimated_date": estimated_delivery}

# Discount / Promo Checker
def apply_discount(base_price, promo_code):
    # Mock promo code validation and application
    discount_codes = {"SAVE10": 0.1, "HOLIDAY20": 0.2}
    discount = discount_codes.get(promo_code.upper(), 0)
    final_price = base_price * (1 - discount)
    return final_price, bool(discount)

# Competitor Price Comparison
def compare_prices(product_name):
    # Mock price comparison
    competitors = {
        "SiteA": 80,
        "SiteB": 75,
        "SiteC": 85,
    }
    return competitors

# Return Policy Checker
def check_return_policy(site_name):
    # Mock return policy information
    policies = {
        "SiteA": "30-day return policy with free return shipping.",
        "SiteB": "15-day return policy with a restocking fee.",
        "SiteC": "45-day return policy with customer-paid return shipping."
    }
    return policies.get(site_name, "Return policy not available.")


# In[ ]:





# In[ ]:




