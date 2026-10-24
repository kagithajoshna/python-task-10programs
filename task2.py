import math

def calculate_attendance_recovery(attended, conducted, target_pct=75.0):
    current_pct = (attended / conducted) * 100.0
    
    if current_pct >= target_pct:
        return current_pct, 0, "Eligible for Examinations"
    
    # Formula derived from: (attended + x) / (conducted + x) >= target / 100
    # x = (target * conducted - 100 * attended) / (100 - target)
    target_fraction = target_pct / 100.0
    required_x = (target_fraction * conducted - attended) / (1.0 - target_fraction)
    additional_classes = math.ceil(required_x)
    
    return current_pct, additional_classes, "Attendance Shortage Detected"

# Test Records: (Name, Attended, Conducted)
students = [
    ("Karthik", 45, 60),  # 75%
    ("Bhavana", 38, 60),  # < 75%
    ("Siddharth", 20, 50) # < 75%
]

print("--- Attendance Recovery Assessment ---")
for name, att, cond in students:
    pct, extra, status = calculate_attendance_recovery(att, cond)
    print(f"Student: {name:<10} | Current: {pct:<5.1f}% | Extra Classes Needed: {extra:<2} | Status: {status}")
