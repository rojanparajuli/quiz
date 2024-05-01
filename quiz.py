import importlib.util
import random
import time

def run_quiz(questions):
    score = 0
    total_questions = len(questions)
    question_keys = list(questions.keys())
    random.shuffle(question_keys)
    
    for question_key in question_keys:
        question = question_key
        answer = questions[question_key]
        
        print(question)
        start_time = time.time()
        user_answer = input("Your answer: ")
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 10
            print("Time taken:", round(elapsed_time, 2), "seconds")
        else:
            print("Incorrect! The correct answer is:", answer)
            score -= 10
            print("Time taken:", round(elapsed_time, 2), "seconds")
        print()
    
    print("Quiz complete!")
    print("You got", score, "points out of", total_questions * 10, "possible points.")
    print("Your score:", score)

questions_file_path = "questions/questions.py"
spec = importlib.util.spec_from_file_location("questions_module", questions_file_path)
questions_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(questions_module)
questions = questions_module.questions

run_quiz(questions)
