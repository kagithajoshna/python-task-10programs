def reconcile_inventory(inventory_records):
    reorder_threshold = 20
    target_stock = 100
    
    report = []
    
    for pid, name, opening, incoming, dispatched, physical in inventory_records:
        expected = opening + incoming - dispatched
        discrepancy = physical - expected
        
        if physical < reorder_threshold:
            reorder_qty = target_stock - physical
        else:
            reorder_qty = 0
            
        report.append({
            "id": pid,
            "name": name,
            "expected": expected,
            "physical": physical,
            "discrepancy": discrepancy,
            "reorder_qty": reorder_qty
        })
        
    return report

# Test Inventory List: (ID, Name, Opening, Incoming, Dispatched, Physical)
data = [
    ("P10", "Mechanical Keyboards", 50, 30, 40, 40), # Expected 40, matches
    ("P11", "Gaming Mice", 15, 50, 55, 8),          # Expected 10, Discrepancy -2, Needs reorder
    ("P12", "USB Hubs", 100, 20, 30, 90)             # Expected 90, matches
]

audit_results = reconcile_inventory(data)

print("--- Warehouse Inventory Audit Report ---")
for r in audit_results:
    flag = f"DISCREPANCY ({r['discrepancy']:+d})" if r['discrepancy'] != 0 else "OK"
    print(f"Item: {r['name']:<20} | Phys Stock: {r['physical']:<3} | Status: {flag:<18} | Reorder Qty: {r['reorder_qty']}")