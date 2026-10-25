def process_university_admissions(applicants):
    eligible = []
    
    for app in applicants:
        name, agg, maths, phys, age = app
        if agg >= 80.0 and maths >= 75:
            eligible.append(app)
            
    # Sort with tie-breakers using bubble sort
    n = len(eligible)
    for i in range(n):
        for j in range(0, n - i - 1):
            c1 = eligible[j]
            c2 = eligible[j + 1]
            
            # Compare Aggregate
            if c1[1] < c2[1]:
                eligible[j], eligible[j+1] = eligible[j+1], eligible[j]
            elif c1[1] == c2[1]:
                # Tie-break 1: Maths score
                if c1[2] < c2[2]:
                    eligible[j], eligible[j+1] = eligible[j+1], eligible[j]
                elif c1[2] == c2[2]:
                    # Tie-break 2: Physics score
                    if c1[3] < c2[3]:
                        eligible[j], eligible[j+1] = eligible[j+1], eligible[j]
                    elif c1[3] == c2[3]:
                        # Tie-break 3: Age
                        if c1[4] < c2[4]:
                            eligible[j], eligible[j+1] = eligible[j+1], eligible[j]

    return eligible

applicant_pool = [
    ("Aditya", 88.5, 90, 85, 18),
    ("Deepak", 92.0, 82, 88, 19),
    ("Kavya", 88.5, 90, 85, 19),  # Same agg, maths, phys as Aditya, but older
    ("Meera", 78.0, 95, 90, 18),  # Ineligible (agg < 80)
    ("Nitin", 88.5, 85, 92, 18)   # Same agg as Aditya/Kavya, lower maths
]

merit_list = process_university_admissions(applicant_pool)

print("--- University Merit Rank List ---")
print(f"{'Rank':<5}{'Name':<10}{'Aggregate':<12}{'Maths':<8}{'Physics':<10}{'Age':<5}")
for rank, c in enumerate(merit_list, 1):
    print(f"{rank:<5}{c[0]:<10}{c[1]:<12.1f}{c[2]:<8}{c[3]:<10}{c[4]:<5}")