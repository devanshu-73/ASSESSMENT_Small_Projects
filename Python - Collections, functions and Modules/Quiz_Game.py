# quiz_game.py
from crud_operations import QuizOperations

def menu():
    print("===== Quiz Game Menu =====")
    print("1. Quiz Master")
    print("2. Quiz Cracker")
    print("3. Exit")

def quiz_master(crud):
    while True:
        print("===== Quiz Master Menu =====")
        print("1. Add Question")
        print("2. View Questions")
        print("3. Delete Question")
        print("4. Exit")

        master_choice = int(input("Enter your choice: "))

        if master_choice == 1:
            crud.add()
            print("Question added successfully!")

        elif master_choice == 2:
            crud.view()

        elif master_choice == 3:
            id_key = int(input("Enter question ID to delete: "))
            crud.delete(id_key)

        elif master_choice == 4:
            print("Exiting the Quiz Game. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

def quiz_cracker(crud):
    while True:
        print("===== Quiz Player Menu =====")
        print("1. Play Quiz")
        print("2. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Play game
            if not crud.data:
                print("No Questions Available")
                exit()
            else:
                for id_key, data_value in crud.data.items():
                    print(f"Question: {data_value['question']}")
                    print("Options:")
                    for i in range(len(data_value['options'])):
                        print(f"{chr(ord('A') + i)}. {data_value['options'][i]}")

                    while True:
                        user_answer = input("Enter your answer (A, B, C, or D): ").upper()

                        if user_answer in ['A', 'B', 'C', 'D']:
                            break
                        else:
                            print("Invalid input. Please enter A, B, C, or D.")

                    correct_option = chr(ord('A') + data_value['correct_option'] - 1)

                    if user_answer == correct_option:
                        print("Correct! Well done!")
                    else:
                 
                        print(f"Wrong! The correct answer is {correct_option}.")

                break

        elif choice == 2:
            break

        else:
            print("Invalid choice. Please enter a valid option.")


def main():
    crud = QuizOperations()

    while True:
        print("======   WELCOME TO TOPS QUIZ  ======")

        menu()
        role = int(input("Enter your role: "))

        if role == 1:
            quiz_master(crud)

        elif role == 2:
            quiz_cracker(crud)

        elif role == 3:
            print("Exiting the Quiz Game. Thank you!")
            break

        else:
            print("Invalid input. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()