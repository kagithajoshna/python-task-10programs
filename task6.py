def simulate_water_tank(capacity, initial_level, flows):
    current_level = initial_level
    log = []
    
    for i, (inflow, outflow) in enumerate(flows, 1):
        net_change = inflow - outflow
        current_level += net_change
        
        status = "Normal"
        spill = 0
        
        if current_level > capacity:
            spill = current_level - capacity
            current_level = capacity
            status = f"OVERFLOW ({spill} L lost)"
        elif current_level <= 0:
            status = "CRITICAL SHORTAGE (Empty)"
            current_level = 0
            
        log.append((i, inflow, outflow, current_level, status))
        
    return log

flow_cycles = [
    (300, 100), # Level: 400
    (500, 100), # Level: 800
    (400, 50),  # Level: 1150 -> Overflow 150
    (100, 950), # Level: 150
    (0, 300)    # Shortage
]

simulation = simulate_water_tank(1000, 200, flow_cycles)

print("--- Multi-Interval Water Tank Operations Log ---")
for t, inf, outf, lvl, state in simulation:
    print(f"Interval {t}: In = {inf:<3}L | Out = {outf:<3}L | Tank Level = {lvl:<4}L | Status: {state}")