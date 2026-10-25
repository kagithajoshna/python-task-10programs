def analyze_performance_trend(student_name, exam_data):
    print(f"--- Performance Trend Analysis for {student_name} ---")
    
    declining_subjects = []
    
    for subject, scores in exam_data.items():
        m1, m2, m3 = scores
        d1 = m2 - m1
        d2 = m3 - m2
        
        if d1 > 0 and d2 > 0:
            trend = "Improving (+)"
        elif d1 < 0 and d2 < 0:
            trend = "Declining (-)"
            declining_subjects.append(subject)
        else:
            trend = "Fluctuating (~)"
            
        print(f"Subject: {subject:<12} | Exam Scores: {scores} | Trend: {trend}")
        
    return declining_subjects

# Test Dataset
student_record = {
    "Mathematics": [55, 68, 82],  # Improving
    "Physics": [75, 65, 52],      # Declining
    "Python": [80, 85, 83]        # Fluctuating
}

weak_subs = analyze_performance_trend("Siddharth", student_record)
print(f"Attention Required in Subjects: {weak_subs}")