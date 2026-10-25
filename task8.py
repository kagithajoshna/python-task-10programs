def find_optimal_route_option(options, fuel_price_per_liter=100.0):
    evaluated = []
    
    for v_name, dist, mileage in options:
        base_fuel = dist / mileage
        total_fuel = base_fuel * 1.10  # 10% reserve margin
        total_cost = total_fuel * fuel_price_per_liter
        
        evaluated.append((v_name, dist, mileage, total_fuel, total_cost))
        
    # Sort by total cost ascending
    evaluated.sort(key=lambda x: x[4])
    return evaluated

route_options = [
    ("SUV", 450, 12),      # 450km @ 12km/l
    ("Sedan", 450, 16),    # 450km @ 16km/l
    ("Hatchback", 480, 20) # 480km alternate route @ 20km/l
]

results = find_optimal_route_option(route_options)

print("--- Route & Vehicle Fuel Efficiency Comparison ---")
for v, d, m, f, c in results:
    print(f"Vehicle: {v:<10} | Dist: {d}km | Mileage: {m}km/L | Fuel (w/ Reserve): {f:.2f}L | Cost: ₹{c:.2f}")

print(f"\nMost Economical Option: {results[0][0]} costing ₹{results[0][4]:.2f}")