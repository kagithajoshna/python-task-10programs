def process_examination_results(student_id, student_name, marks_dict):
    pass_mark = 40
    max_mark = 100
    max_grace_pool = 10
    used_grace = 0
    
    updated_marks = {}
    
    for subject, score in marks_dict.items():
        if score < pass_mark and score >= (pass_mark - 5):
            needed_grace = pass_mark - score
            if used_grace + needed_grace <= max_grace_pool:
                score += needed_grace
                used_grace += needed_grace
        
        # Enforce max limit cap
        updated_marks[subject] = min(score, max_mark)
        
    all_passed = all(m >= pass_mark for m in updated_marks.values())
    total_marks = sum(updated_marks.values())
    percentage = total_marks / len(updated_marks)
    
    if all_passed:
        if percentage >= 75:
            classification = "Passed with Distinction"
        elif percentage >= 60:
            classification = "Passed in First Class"
        else:
            classification = "Pass"
    else:
        classification = "Fail (Re-appear required)"
        
    return updated_marks, used_grace, percentage, classification

# Test Data
student_marks = {"Maths": 36, "Physics": 38, "Chemistry": 72, "English": 85, "Python": 95}

final_marks, grace_given, pct, result = process_examination_results("ST102", "Ananya", student_marks)

print("--- Examination Grace-Mark Audit ---")
print(f"Student: Ananya | Total Grace Awarded: {grace_given} marks")
print("Adjusted Subject Scores:")
for sub, sc in final_marks.items():
    print(f"  {sub:<12}: {sc}")
print(f"Overall Percentage: {pct:.2f}%")
print(f"Final Outcome     : {result}")