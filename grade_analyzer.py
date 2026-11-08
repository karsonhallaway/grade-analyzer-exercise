# --- Data --
# Store a list of numbers in variable scores
scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

# organize scores into letter grade categories
a_grades = []
b_grades = []
c_grades = []
d_grades = []
f_grades = []

# number of passing and failing grades
passing_count = []
failing_count = []

for score in scores:
    if score >= 60:
        passing_count.append(score)
    else:
        failing_count.append(score)

# loop through scores. append each score to letter grade list.
for score in scores:
    if score >= 90:
        a_grades.append(score)
    elif score >= 80:
        b_grades.append(score)
    elif score >= 70:
        c_grades.append(score)
    elif score >= 60:
        d_grades.append(score)
    else:
        f_grades.append(score)


# --- Calculated Data ---
# total number of scores
total_scores = len(scores)

# average
avg = sum(scores) / len(scores)

# highest
highest_score = max(scores)

# lowest
lowest_score = min(scores)


# --- Display Main Menu ---
def main():
    print("\n=== Grade Analyzer ===")
    print(f"Total scores: {total_scores}")
    print(f"Average: {float(avg):.1f}")
    print(f"Highest: {highest_score}")
    print(f"Lowest: {lowest_score}")
    print(f"Passing: {len(passing_count)} ({sum(passing_count) / float(len(passing_count)):.1f})")
    print(f"Failing: {len(failing_count)} ({sum(failing_count) / float(len(failing_count)):.1f})")
    
    print("\nGrade Distribution:")
    print(f"A: {len(a_grades)} students")
    print(f"A: {len(b_grades)} students")
    print(f"C: {len(c_grades)} students")
    print(f"D: {len(d_grades)} students")
    print(f"F: {len(f_grades)} students")

while scores:
    
    main()
        
    print("\n--- Add More Scores ---")
    try:
        new_score = input("Enter a new score (or 'done' to quit): ").strip() 
        if new_score.lower() == 'done':
            break
        new_score = int(new_score)
        
        if new_score > 100:
            print("Entry must be between 1 - 100. Try again")
        elif new_score >= 1:
            scores.append(new_score)
        else:
            print("Entry must be positive. Try again.")
        new_avg = sum(scores) / len(scores)
    except ValueError:
        print("Invalid score. Please enter a number or 'done'.")
        
    print(f"Updated average: {float(new_avg):.1f}")
    
    print(f"\nFinal average: {float(new_avg):.1f}")
    


        
    
