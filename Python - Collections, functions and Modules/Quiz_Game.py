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

        ch = int(input("Enter your choice: "))

        if ch == 1:
            crud.add()
            print("Question added successfully!")

        elif ch == 2:
            crud.view()

        elif ch == 3:
            id_key = int(input("Enter question ID to delete: "))
            crud.delete(id_key)

        elif ch == 4:
            print("Exiting the Quiz Game.Thank you!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

def quiz_cracker(crud):
    while True:
        print("===== Quiz Cracker Menu =====")
        print("1. Play Quiz")
        print("2. Exit")

        ch = int(input("Enter your choice: "))

        if ch == 1:
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
                        
                    user_answer = input("Enter your answer : ") #print("Values :",data_value)
                    
                    if user_answer == data_value['correct_option']:
                        print("Correct! Well done!")
                    else:
                        print(f"Wrong! The correct answer is {data_value['correct_option']}.")
                break

        elif ch == 2:
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
