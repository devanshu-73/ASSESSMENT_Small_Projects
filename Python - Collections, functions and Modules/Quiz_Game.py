from crud_operations import QuizOperations

def display_menu():
    print("\n===== Quiz Game Menu =====")
    print("1. Quiz Master")
    print("2. Quiz Cracker")
    print("3. Exit")

def get_user_input(prompt, is_integer=True):
    while True:
        user_input = input(prompt)
        if user_input.strip():
            if is_integer and not user_input.isdigit():
                print("Invalid input. Please enter a valid number.")
            else:
                return int(user_input) if is_integer else user_input
        else:
            print("Invalid input. Please try again.")

def add_question(quiz_operations):
    question_id = str(len(quiz_operations.quiz_data) + 1)
    question = get_user_input(f"Enter question #{question_id}: ")
    
    options = []
    for i in range(4):
        option = get_user_input(f"Enter option {i + 1}: ", is_integer=False)
        options.append(option)
    
    correct_option = get_user_input("Enter correct option number: ", is_integer=True)

    quiz_operations.add_question(question_id, question, options, correct_option)
    print("Question added successfully!")

def view_questions(quiz_operations):
    if not quiz_operations.quiz_data:
        print("No questions available.")
    else:
        quiz_operations.view_questions()

def delete_question(quiz_operations):
    question_id = get_user_input("Enter question ID to delete: ")
    if quiz_operations.delete_question(question_id):
        print("Question deleted successfully!")
    else:
        print("Question ID not found.")

def quiz_cracker_operations(quiz_operations):
    while True:
        print("===== Quiz Cracker Menu =====")
        print("1. View Questions")
        print("2. Exit")

        choice = get_user_input("Enter your choice: ", is_integer=True)

        if choice == 1:
            view_questions(quiz_operations)
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

        master_choice = get_user_input("Enter your choice: ", is_integer=True)

        if master_choice == 1:
            add_question(quiz_operations)
        elif master_choice == 2:
            view_questions(quiz_operations)
        elif master_choice == 3:
            delete_question(quiz_operations)
        elif master_choice == 4:
            print("Exiting the Quiz Game. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def main():
    quiz_operations = QuizOperations()

    while True:
        print("======   WELCOME TO TOPS QUIZ GAMING CHALLENGE   ======")
        
        display_menu()
        role = get_user_input("Enter your role: ", is_integer=True)

        if role == 1:
            quiz_master_operations(quiz_operations)
        elif role == 2:
            quiz_cracker_operations(quiz_operations)
        elif role == 3:
            print("Exiting the Quiz Game. Thank you!")
            break
        else:
            print("Invalid input. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
