#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tools import *


# In[3]:


class FashionShoppingAgent:
    def __init__(self):
        self.tools = {
            "search_products": search_products,
            "estimate_shipping": estimate_shipping,
            "apply_discount": apply_discount,
            "compare_prices": compare_prices,
            "check_return_policy": check_return_policy
        }
    
    def handle_query(self, user_query):
        if "floral skirt" in user_query.lower() and "under $40" in user_query.lower():
            products = self.tools["search_products"]("Floral Skirt", "Red", (0, 40), "S")
            if products:
                product = products[0]
                final_price, discount_applied = self.tools["apply_discount"](product["price"], "SAVE10")
                response = (f"I found a floral skirt for ${product['price']} (size {product['size']}, "
                            f"in stock). After applying the discount code 'SAVE10', "
                            f"the final price is ${final_price:.2f}.")
            else:
                response = "No matching floral skirts found under $40."
            return response
        
        if "white sneakers" in user_query.lower() and "under $70" in user_query.lower() and "by Friday" in user_query.lower():
            products = self.tools["search_products"]("White Sneakers", "White", (0, 70), "8")
            if products:
                product = products[0]
                estimated_shipping = self.tools["estimate_shipping"]("Sholinganallur, Tamil Nadu, India", datetime.now() + timedelta(days=2))
                response = (f"I found white sneakers for ${product['price']} (size {product['size']}, in stock). "
                            f"Estimated shipping cost: ${estimated_shipping['cost']:.2f}, "
                            f"Estimated delivery date: {estimated_shipping['estimated_date'].strftime('%Y-%m-%d')}, "
                            f"Shipping feasible: {'Yes' if estimated_shipping['feasible'] else 'No'}.")
            else:
                response = "No matching white sneakers found under $70."
            return response

        if "casual denim jacket" in user_query.lower():
            prices = self.tools["compare_prices"]("Casual Denim Jacket")
            response = f"Price comparison across competitors: {prices}."
            return response

        if "cocktail dress" in user_query.lower() and "SiteB" in user_query.lower():
            policy = self.tools["check_return_policy"]("SiteB")
            response = f"Return policy for SiteB: {policy}."
            return response
        
        return "I'm sorry, I couldn't understand your query. Could you please rephrase it?"


# In[4]:


if __name__ == "__main__":
    user_queries = [
        "Find a floral skirt under $40 in size S. Is it in stock, and can I apply a discount code 'SAVE10'?",
        "I need white sneakers (size 8) for under $70 that can arrive by Friday.",
        "I found a ‘casual denim jacket’ at $80 on SiteA. Any better deals?",
        "I want to buy a cocktail dress from SiteB, but only if returns are hassle-free. Do they accept returns?"
    ]


# In[5]:


agent = FashionShoppingAgent()
for query in user_queries:
        print(agent.handle_query(query))


# In[ ]:




