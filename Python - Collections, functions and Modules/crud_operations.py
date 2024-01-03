# crud_operations.py

class QuizOperations:
    def __init__(self):
        self.quiz_data = {}

    def add_question(self, question, options, correct_option):
        # Use an incremental counter for question_id
        question_id = len(self.quiz_data) + 1
        self.quiz_data[question_id] = {
            'question': question,
            'options': options,
            'correct_option': correct_option
        }

    def view_questions(self):
        if not self.quiz_data:
            print("No questions available.")
            exit()
        else:
            for question_id, data in self.quiz_data.items():
                print(f"\nID: {question_id}, Question: {data['question']}")
                print("Options:")
                for i in range(len(data['options'])):
                    print(f"{chr(ord('A') + i)}. {data['options'][i]}")
                    
    def delete_question(self, question_id):
        if question_id in self.quiz_data:
            del self.quiz_data[question_id]
            return True
        else:
            return False
