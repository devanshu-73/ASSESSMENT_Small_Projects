from quiz_operations import QuizOperations

# Initialize quiz and questions
quiz = QuizOperations()
questions = {}  # Dictionary to store questions

# Function to display the menu
def display_menu():
    print("\n===== Quiz Game Menu =====")
    print("1. Add Question")
    print("2. View Questions")
    print("3. Delete Question")
    print("4. Play Quiz")
    print("5. Exit")

# Function to get user input with validation
def get_user_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        if user_input.strip() and validation_func(user_input):
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

# Function to initialize quiz and questions
def initialize_quiz():
    global quiz, questions
    quiz = QuizOperations()
    questions = {}

# Function to handle Quiz Master operations
def quiz_master_operations(quiz, questions):
    question_id = str(len(questions) + 1)  # Using the length of the dictionary for question IDs
    question = input(f"Enter question #{question_id}: ")
    options = input("Enter options separated by commas: ").split(',')
    correct_option = get_user_input("Enter correct option: ", lambda x: x in options)

    questions[question_id] = {
        'question': question,
        'options': options,
        'correct_option': correct_option
    }

    print("Question added successfully!")

# Function to handle Quiz Cracker operations
def quiz_cracker_operations(questions):
    if not questions:
        print("No questions available.")
        return

    for question_id, details in questions.items():
        print(f"ID: {question_id}")
        print(f"Question: {details['question']}")
        print("Options:", ', '.join(details['options']))
        print(f"Correct Option: {details['correct_option']}")

# Function to play quiz
def play_quiz(questions):
    if not questions:
        print("No questions available.")
        return

    for question_id, details in questions.items():
        print(f"\nID: {question_id}")
        print(f"Question: {details['question']}")
        print("Options:", ', '.join(details['options']))

# Main program
while True:
    print("======   WELCOME TO TOPS QUIZ GAMING CHALLENGE   ======")
    print('''Select your role : 
                 -> Quiz Master  (Press 1)
                 -> Quiz Cracker (Press 2)
                 -> Exit (Press 0)''')

    role = get_user_input("Enter your role: ", lambda x: x in ['0', '1', '2'])

    if role == '0':
        print("Exiting the Quiz Game. Thank you!")
        break    
    elif role == '1':
        quiz_master_operations(quiz, questions)
    elif role == '2':
        quiz_cracker_operations(questions)
    else:
        print("You entered an incorrect input. Please choose 1, 2, or 0.")
        continue  # Go back to the main menu

    initialize_quiz()  # Initialize quiz and questions

    while True:
        display_menu()
        choice = get_user_input("Enter your choice: ", is_valid_integer)

        if choice == '3':
            question_id = get_user_input("Enter question ID to delete: ", is_valid_integer)
            confirmation = get_user_input("Are you sure you want to delete this question? (Y/N): ", is_valid_confirmation)

            if confirmation == 'y':
                if questions.pop(question_id, None):
                    print("Question deleted successfully!")
                else:
                    print("Question ID not found.")

        elif choice == '4':
            play_quiz(questions)

        elif choice == '5':
            print("Exiting the Quiz Game. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
