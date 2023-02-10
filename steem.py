def main():
    print(
        "This program is an implementation of the Rosenberg Self-Esteem Scale. \nThis program will show you ten statements that you could possibly apply to yourself.\nPlease rate how much you agree with each of the statements by responding with one of these four letters:"
    )

    print("\nD means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")
    create_question_list()

def create_question_list():
    questions=[]
    questions.append("1. I feel that I am a person of worth, at least on an equal plane with others.")
    questions.append("2. I feel that I have a number of good qualities.")
    questions.append("3. All in all, I am inclined to feel that I am a failure.")
    questions.append("4. I am able to do things as well as most other people.")
    questions.append("5. I feel I do not have much to be proud of.")
    questions.append("6. I take a positive attitude toward myself.")
    questions.append("7. On the whole, I am satisfied with myself.")
    questions.append("8. I wish I could have more respect for myself.")
    questions.append("9. I certainly feel useless at times.")
    questions.append("10. At times I think I am no good at all.")    
    execute_questions(questions)


def execute_questions(questions):
    answers = []
    for i in questions:
        print (i)
        user_answer=""
        while user_answer not in ("D","d","a","A"):
            user_answer=input("Enter D, d, a, or A: ")
        answers.append(user_answer)

    compute_answers(questions,answers)


def compute_answers(questions, answers):
    #1, 2, 4, 6, 7
    points=0
    for i in (0,1,3,5,6):
        if answers[i]=="d": # Disagree 1
            points+=1
        elif answers[i]=="a": # Agree 2
            points+=2
        elif answers[i]=="A": # Strongly Agree 3
            points+=3
            
    #numbers 3, 5, 8, 9, 10
    for i in (2,4,7,8,9):
        if answers[i]=="D": # Strongly Disagree
            points+=3
        elif answers[i]=="d": # Disagree 1
            points+=2
        elif answers[i]=="a": # Agree 2
            points+=1

    
    print_point(points)


def print_point(points):
    print(points)

    print(f"Your score is {points}.")
    print("A score below 15 may indicate problematic low self-esteem.")


main()
