def optimize_shopping_basket(budget, items):
    # items structure: list of dicts ordered by priority descending
    def calc_total(basket):
        return sum(i["qty"] * i["price"] for i in basket)
    
    current_cost = calc_total(items)
    
    # Prune items from lowest priority (end of list) if over budget
    while current_cost > budget:
        pruned = False
        for i in range(len(items) - 1, -1, -1):
            if items[i]["qty"] > 0:
                items[i]["qty"] -= 1
                pruned = True
                break
        current_cost = calc_total(items)
        if not pruned:
            break  # Unable to reduce further
            
    return items, current_cost

shopping_list = [
    {"name": "Textbooks", "price": 800, "qty": 2},  # Priority 1 (Cost 1600)
    {"name": "Notebooks", "price": 100, "qty": 5},  # Priority 2 (Cost 500)
    {"name": "Pens Pack", "price": 150, "qty": 3}   # Priority 3 (Cost 450)
] # Initial Total = 2550

budget_limit = 2000.0
adjusted_cart, final_total = optimize_shopping_basket(budget_limit, shopping_list)

print(f"--- Budget Optimization (Budget: ₹{budget_limit:.2f}) ---")
print("Adjusted Basket Contents:")
for item in adjusted_cart:
    print(f"  Item: {item['name']:<12} | Qty: {item['qty']:<2} | Total: ₹{item['qty'] * item['price']}")
print(f"Final Cart Total: ₹{final_total:.2f}")