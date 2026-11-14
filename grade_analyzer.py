# --- Data ---
# Store a list of numbers in variable scores
scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]


# --- Analyze and Display ---
def analyze(scores):
    # organize scores into letter grade categories
    a_grades = []
    b_grades = []
    c_grades = []
    d_grades = []
    f_grades = []

    # number of passing grades
    passing_count = sum(score >= 60 for score in scores)
    failing_count = len(scores) - passing_count 
    


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
    total_scores = len(scores)
    avg = sum(scores) / total_scores
    highest_score = max(scores)
    lowest_score = min(scores)

    print("\n=== Grade Analyzer ===")
    print(f"Total scores: {total_scores}")
    print(f"Average: {avg:.1f}")
    print(f"Highest: {highest_score}")
    print(f"Lowest: {lowest_score}")
    print(f"Passing: {passing_count / total_scores:.1%}")
    print(f"Failing: {failing_count / total_scores:.1%}")

    print("\n--- Grade Distribution:\n")
    print(f"A: {len(a_grades)} students")
    print(f"B: {len(b_grades)} students")
    print(f"C: {len(c_grades)} students")
    print(f"D: {len(d_grades)} students")
    print(f"F: {len(f_grades)} students")


analyze(scores)

def main():
    while True:
        print("\n--- Add More Scores ---")
        new_avg = sum(scores) / len(scores) 

        try:
            new_score = input("Enter a new score (or 'done' to quit): ").strip()
            if new_score.lower() == 'done':
                break
            new_score = int(new_score)

            if new_score > 100:
                print("Entry must be between 0 - 100. Try again")
            elif new_score >= 0:
                scores.append(new_score)
            else:
                print("Entry must be positive. Try again.")
        except ValueError:
            print("Invalid score. Please enter a number or 'done'.")
            

        print(f"Updated average: {sum(scores) / len(scores):.1f}")

    # show the full analysis again with the new scores included
    analyze(scores)

    print(f"\nFinal Average: {new_avg:.1f}\n")

if __name__ == "__main__":
    main() 