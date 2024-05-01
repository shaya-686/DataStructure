import json
import random


class Questionare:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions


class QuestionareResults:
    results_file = "questionare_results.json"
    answers = ["a", "b", "c", "d"]

    def __init__(self):
        self.results = []

    def add_results(self, questionare):
        answers_dct = []
        for question in questionare.questions:
            answers_dct.append({question: random.choice(self.answers)})
        record = {"name": questionare.name,
                  "questions": answers_dct}
        self.results.append(record)

    def export_to_json(self):
        with open(self.results_file, 'w') as file:
            json.dump(self.results, file, indent=4)

    def import_results(self):
        with open(self.results_file, 'r') as file:
            results = json.load(file)
        return results


quest1 = Questionare("first_questionare", ["q_1_1", "q_1_2", "q_1_3"])
quest2 = Questionare("second_questionare", ["q_2_1", "q_2_2", "q_2_3"])

quest_result = QuestionareResults()
quest_result.add_results(quest1)
quest_result.add_results(quest2)

quest_result.export_to_json()
print(quest_result.import_results())
