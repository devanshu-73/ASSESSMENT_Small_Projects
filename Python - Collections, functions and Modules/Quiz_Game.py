# quiz_game.py
from crud_operations import QuizOperations

def display_menu():
    print("\n===== Quiz Game Menu =====")
    print("1. Quiz Master")
    print("2. Quiz Player")
    print("3. Exit")

def quiz_player_operations(quiz_operations):
    while True:
        print("===== Quiz Player Menu =====")
        print("1. Play Quiz")
        print("2. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Play game
            if not quiz_operations.quiz_data:
                print("No Questions Available")
            else:
                for question_id, question_data in quiz_operations.quiz_data.items():
                    print(f"\nQuestion: {question_data['question']}")
                    print("Options:")
                    for i in range(len(question_data['options'])):
                        print(f"{chr(ord('A') + i)}. {question_data['options'][i]}")

                    user_answer = input("Enter your answer (A, B, C, or D): ").upper()
                    correct_option = chr(ord('A') + question_data['correct_option'] - 1)

                    if user_answer == correct_option:
                        print("Correct! Well done!")
                    else:
                        print(f"Wrong! The correct answer is {correct_option}.")

                break  # Break the loop after playing the game once

        elif choice == 2:
            break

        else:
            print("Invalid choice. Please enter a valid option.")

def quiz_master_operations(quiz_operations):
    while True:
        print("===== Quiz Master Menu =====")
        print("1. Add Question")
        print("2. View Questions")
        print("3. Delete Question")
        print("4. Exit")

        master_choice = int(input("Enter your choice: "))

        if master_choice == 1:
            # Add a new question
            question = input("Enter the question: ")
            options = [input(f"Enter option {chr(ord('A') + i)}: ") for i in range(4)]
            correct_option = int(input("Enter correct option number (1 to 4): "))

            quiz_operations.add_question(question, options, correct_option)
            print("Question added successfully!")

        elif master_choice == 2:
            quiz_operations.view_questions()

        elif master_choice == 3:
            question_id = int(input("Enter question ID to delete: "))
            if quiz_operations.delete_question(question_id):
                print("Question deleted successfully!")
            else:
                print("Question ID not found.")

        elif master_choice == 4:
            print("Exiting the Quiz Game. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

def main():
    quiz_operations = QuizOperations()

    while True:
        print("======   WELCOME TO QUIZ MANIA   ======")

        display_menu()
        role = int(input("Enter your role: "))

        if role == 1:
            quiz_master_operations(quiz_operations)

        elif role == 2:
            quiz_player_operations(quiz_operations)

        elif role == 3:
            print("Exiting the Quiz Game. Thank you!")
            break

        else:
            print("Invalid input. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
