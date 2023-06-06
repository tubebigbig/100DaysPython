scores_input = input("Input a list of student scores ").split()
student_scores = [int(n) for n in scores_input]
for n in range(0, len(scores_input)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")
