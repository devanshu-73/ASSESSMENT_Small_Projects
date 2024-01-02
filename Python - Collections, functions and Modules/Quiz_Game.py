from quiz_operations import QuizOperations

# Function to display the menu
print("======   WELCOME TO TOPS QUIZ GAMING CHALLENGE   ======")
print('''Select your role : 
                 -> Quiz Master  (Press 1)
                 -> Quiz Cracker (Press 2)''')
role = int(input("Enter your role : "))

def display_menu():
    print("\n===== Quiz Game Menu =====")
    print("1. Add Question")
    print("2. View Questions")
    print("3. Delete Question")
    print("4. Exit")

# Function to get user input with validation
def get_user_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

# Validation function for integer input
def is_valid_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# Validation function for Y/N input
def is_valid_confirmation(value):
    return value.lower() in ['y', 'n']

# Main program
if __name__ == "__main__":
    quiz = QuizOperations()

    while True:
        display_menu()
        choice = get_user_input("Enter your choice: ", is_valid_integer)

        if choice == '1':
            question_id = get_user_input("Enter question ID: ", is_valid_integer)
            question = input("Enter the question: ")
            options = input("Enter options separated by commas: ").split(',')
            correct_option = get_user_input("Enter correct option: ", lambda x: x in options)

            quiz.add_question(question_id, question, options, correct_option)
            print("Question added successfully!")

        elif choice == '2':
            quiz.view_questions()

        elif choice == '3':
            question_id = get_user_input("Enter question ID to delete: ", is_valid_integer)
            confirmation = get_user_input("Are you sure you want to delete this question? (Y/N): ", is_valid_confirmation)

            if confirmation == 'y':
                if quiz.delete_question(question_id):
                    print("Question deleted successfully!")
                else:
                    print("Question ID not found.")

        elif choice == '4':
            print("Exiting the Quiz Game. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

    # Additional logic for logging and further processing can be added here.
