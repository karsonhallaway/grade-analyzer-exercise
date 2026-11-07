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
passing_count = 0
failing_count = 0

for score in scores:
    if score >= 60:
        passing_count += 1
    else:
        failing_count += 1

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
avg = (sum(scores) / float(len(scores)))

# highest
highest_score = max(scores)

# lowest
lowest_score = min(scores)


# while Display is true: 
    # score total
    # average
    # highest
    # lowest
    # number of passing scores
    # number of failing scores
    # total number of scores in each grade category
    
    # while prompt is add new score:
        # prompt the user add a new score or exit
        # calculate average and assign it to update_average
        # print the new average 
    # otherwise exit
    
    # print final average
    

        
    
