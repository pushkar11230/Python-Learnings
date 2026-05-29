def quiz_code():
    gen_questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Jupiter", "C. Mars", "D. Saturn"],
            "answer": "C"
        },
        {
            "question": "How many continents are there on Earth?",
            "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
            "answer": "C"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. J.K. Rowling"],
            "answer": "B"
        },
        {
            "question": "Which is the largest ocean in the world?",
            "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "What is the chemical symbol for Gold?",
            "options": ["A. Ag", "B. Au", "C. Gd", "D. Go"],
            "answer": "B"
        },
        {
            "question": "Which language is primarily used for Data Analysis?",
            "options": ["A. Python", "B. HTML", "C. CSS", "D. XML"],
            "answer": "A"
        },
        {
            "question": "How many days are there in a leap year?",
            "options": ["A. 364", "B. 365", "C. 366", "D. 367"],
            "answer": "C"
        },
        {
            "question": "Which country is famous for the Eiffel Tower?",
            "options": ["A. Germany", "B. Italy", "C. France", "D. Spain"],
            "answer": "C"
        },
        {
            "question": "What is the square root of 144?",
            "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
            "answer": "C"
        }
    ]

    score = 0

    for index, q in enumerate(gen_questions, start = 1):
        print(f"\nQ{index}. {q['question']}")

        for opt in q["options"]:
            print(opt)
        
        while True:
            user_answer = input("\nEnter your answer (A/B/C/D): ").strip().upper()

            if user_answer in ("A", "B", "C", "D"):
                break

            print("\nWrong input! Please enter A, B, C, or D.")

        if user_answer == q["answer"]:
            print("\nCorrect answer ✔")
            score += 10
        else:
            print("\nWrong answer ✖")
            print(f"Correct answer was: {q['answer']}")
        
        if index != len(gen_questions):
            input("\nPress Enter for next question")

    print(f"\nYour final score is: {score}")

quiz_code()