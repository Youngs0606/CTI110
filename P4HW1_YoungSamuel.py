# CTI-110
# P4HW1 - Score List
# Young, Samuel   
# 5-5-23
#


num_scores = int(input("How many scores do you want to enter? "))

scores = []
for i in range(1, num_scores+1):
    while True:
        score = float(input(f"Enter score #{i}: "))
        if score >= 0 and score <= 100:
            scores.append(score)
            break
        else:
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            continue

print("--------------Results--------------")
print(f"Lowest Score  : {min(scores)}")
scores.remove(min(scores))
print(f"Modified List : {scores}")
average_score = sum(scores)/len(scores)
print(f"Scores Average: {average_score:.2f}")
if average_score >= 90:
    print("Grade         : A")
elif average_score >= 80:
    print("Grade         : B")
elif average_score >= 70:
    print("Grade         : C")
elif average_score >= 60:
    print("Grade         : D")
else:
    print("Grade         : F")
print("------------------------------------")
