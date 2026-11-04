def calculate_parking_fee(vehicle_type, entry_hr, exit_hr):
    rates = {
        "Bike": {"rate": 20, "cap": 150},
        "Car": {"rate": 50, "cap": 400},
        "Bus": {"rate": 100, "cap": 800}
    }
    
    if vehicle_type not in rates:
        return "Invalid Vehicle Category"
        
    if entry_hr < 0 or entry_hr > 23 or exit_hr < 0 or exit_hr > 23:
        return "Invalid Time Input"
        
    if exit_hr <= entry_hr:
        duration = (exit_hr + 24) - entry_hr
    else:
        duration = exit_hr - entry_hr
        
    v_info = rates[vehicle_type]
    base_fee = min(duration * v_info["rate"], v_info["cap"])
    
    overnight_surcharge = 200.0 if duration > 12 else 0.0
    total_fee = base_fee + overnight_surcharge
    
    return duration, total_fee

test_cases = [
    ("Car", 9, 14),   # 5 hours
    ("Bike", 10, 22), # 12 hours
    ("Car", 18, 8),   # 14 hours overnight
]

print("--- Smart Parking Billing Engine ---")
for vtype, entry, exit_time in test_cases:
    dur, fee = calculate_parking_fee(vtype, entry, exit_time)
    print(f"Vehicle: {vtype:<5} | In: {entry:02d}:00 | Out: {exit_time:02d}:00 | Duration: {dur:<2} hrs | Total Fee: ₹{fee:.2f}")