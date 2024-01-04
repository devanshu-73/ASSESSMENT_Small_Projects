# crud_operations.py

class QuizOperations:
    def __init__(self):
        #Auto Create Blank Dict
        self.data = {}

    def add(self):
        # Add New Question
        id_key = len(self.data) + 1
        options = []
        question = input("Enter the question: ")
        
        for i in range(4):
            options.append(input(f"Enter option {chr(ord('A') + i)}: ")) 
            
        correct_option = input("Enter Correct Answer: ")

        self.data[id_key] = {
            'question': question,
            'options': options,
            'correct_option': correct_option
        }

    def view(self):
        #View Questions
        if not self.data:
            print("No questions available.")
            exit()
        else:
            for id_key, data_value in self.data.items():
                print(f"ID: {id_key}, Question: {data_value['question']}")
                print("Options:")
                for i in range(len(data_value['options'])):
                    print(f"{chr(ord('A') + i)}. {data_value['options'][i]}")
                    
    def delete(self, id_key):
        # Delete Question
        if id_key in self.data:
            del self.data[id_key]
            print("Question deleted successfully!")
        else:
            print("Question ID not found or U entered Wrong input.")
