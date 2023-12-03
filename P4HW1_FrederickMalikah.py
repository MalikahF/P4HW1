#CTI-110
#P4HW1 - Score List
#Malikah Frederick
#12-03-2023

# Pseudocode:
# 1. Prompt the user to enter the number of scores.
# 2. Create an empty list to store the scores.
# 3. Use a loop to collect valid scores from the user.
#    a. Inside the loop, ask the user to enter a score.
#    b. Check if the score is valid (between 0 and 100).
#    c. If valid, add the score to the list.
#    d. If not valid, notify the user and ask for a valid score.
# 4. Calculate and display the lowest score entered.
# 5. Drop the lowest score from the list.
# 6. Display the modified score list.
# 7. Calculate and display the average of scores in the modified list.
# 8. Determine the letter grade for the calculated average and display it.

def calculate_average(score_list):
    total = sum(score_list)
    average = total / len(score_list)
    return average

def determine_letter_grade(average):
    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'

def main():
    print("Score List Program")

    # Step 1
    num_scores = int(input("Enter the number of scores you would like to enter: "))

    # Step 2
    score_list = []

    # Step 3
    for i in range(1, num_scores + 1):
        while True:
            try:
                # Step 3a
                score = float(input(f"Enter score #{i}: "))

                # Step 3b
                if 0 <= score <= 100:
                    # Step 3c
                    score_list.append(score)
                    break
                else:
                    # Step 3d
                    print("Invalid score. Please enter a score between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid numeric score.")

    # Step 4
    lowest_score = min(score_list)
    print(f"\nLowest score entered: {lowest_score}")

    # Step 5
    score_list.remove(lowest_score)

    # Step 6
    print("Score List after dropping lowest score:")
    for i, score in enumerate(score_list, start=1):
        print(f"Score {i}: {score}")

    # Step 7
    average = calculate_average(score_list)
    print(f"\nAverage of scores in modified list: {average:.2f}")

    # Step 8
    letter_grade = determine_letter_grade(average)
    print(f"Letter Grade: {letter_grade}")

if __name__ == "__main__":
    main()
