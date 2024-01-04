# crud_operations.py

class QuizOperations:
    def __init__(self):
        self.data = {}

    def add(self, question, options, correct_option):
        question_id = len(self.data) + 1
        self.data[question_id] = {
            'question': question,
            'options': options,
            'correct_option': correct_option
        }

    def view(self):
        if not self.data:
            print("No questions available.")
            exit()
        else:
            for question_id, data in self.data.items():
                print(f"ID: {question_id}, Question: {data['question']}")
                print("Options:")
                for i in range(len(data['options'])):
                    print(f"{chr(ord('A') + i)}. {data['options'][i]}")
                    
    def delete(self, question_id):
        if question_id in self.data:
            del self.data[question_id]
            return True
        else:
            return False

