# (Business logic module)
class QuizOperations:
    def __init__(self):
        self.quiz_data = {}

    def add_question(self, question_id, question, options, correct_option):
        self.quiz_data[question_id] = {
            'question': question,
            'options': options,
            'correct_option': correct_option
        }

    def view_questions(self):
        for question_id, data in self.quiz_data.items():
            print(f"ID: {question_id}, Question: {data['question']}")
            print("Options:", ', '.join(data['options']))
            print()

    def delete_question(self, question_id):
        if question_id in self.quiz_data:
            del self.quiz_data[question_id]
            return True
        else:
            return False
