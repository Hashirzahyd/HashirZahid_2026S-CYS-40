import time

# credentials
ADMIN_USER = "ecat_admin"
ADMIN_PASS = "ecat@2026"
STU_USER = "student"
STU_PASS = "student123"

# question bank
questions = [
    {"subject": "Physics",     "question": "SI unit of force?",                         "choices": {"A": "Joule", "B": "Newton", "C": "Watt", "D": "Pascal"},              "answer": "B"},
    {"subject": "Chemistry",   "question": "Chemical formula of water?",                "choices": {"A": "H2O2",  "B": "CO2",    "C": "H2O",  "D": "NaCl"},               "answer": "C"},
    {"subject": "Mathematics", "question": "Value of pi (approx)?",                     "choices": {"A": "3.14",  "B": "2.71",   "C": "1.41", "D": "1.73"},               "answer": "A"},
    {"subject": "Physics",     "question": "Speed of light in vacuum?",                 "choices": {"A": "3x10^6 m/s", "B": "3x10^8 m/s", "C": "3x10^10 m/s", "D": "3x10^4 m/s"}, "answer": "B"},
    {"subject": "Chemistry",   "question": "Most abundant gas in atmosphere?",          "choices": {"A": "Oxygen", "B": "CO2", "C": "Hydrogen", "D": "Nitrogen"},          "answer": "D"},
    {"subject": "Mathematics", "question": "Square root of 144?",                       "choices": {"A": "11", "B": "12", "C": "13", "D": "14"},                          "answer": "B"},
    {"subject": "Physics",     "question": "Every action has equal and opposite reaction?", "choices": {"A": "Newton 1st", "B": "Newton 2nd", "C": "Newton 3rd", "D": "Hooke's Law"}, "answer": "C"},
    {"subject": "Chemistry",   "question": "Atomic number of Carbon?",                  "choices": {"A": "4", "B": "6", "C": "8", "D": "12"},                             "answer": "B"},
    {"subject": "Mathematics", "question": "15% of 200?",                               "choices": {"A": "25", "B": "30", "C": "35", "D": "40"},                          "answer": "B"},
    {"subject": "Physics",     "question": "Energy of a moving object?",                "choices": {"A": "Potential", "B": "Chemical", "C": "Kinetic", "D": "Nuclear"},   "answer": "C"},
    {"subject": "Chemistry",   "question": "pH of pure water?",                         "choices": {"A": "5", "B": "6", "C": "7", "D": "8"},                              "answer": "C"},
    {"subject": "Mathematics", "question": "Degrees in a right angle?",                 "choices": {"A": "45", "B": "60", "C": "90", "D": "180"},                         "answer": "C"},
]

all_results = []

def line():
    print("=" * 50)

def grade(p):
    if p >= 80: return "EXCELLENT"
    elif p >= 65: return "GOOD"
    elif p >= 50: return "AVERAGE"
    else: return "BELOW AVERAGE"

def login(user, passw, role):
    line()
    print(f"  {role} LOGIN")
    line()
    attempts = 0
    while attempts < 3:
        u = input("Username: ").strip()
        p = input("Password: ").strip()
        if u == user and p == passw:
            print("  Login successful!")
            time.sleep(1)
            return True
        attempts = attempts + 1
        left = 3 - attempts
        if left > 0:
            print(f"  Wrong credentials. {left} attempt(s) left.")
        else:
            print("  Access locked.")
    return False

# ---- ADMIN FUNCTIONS ----

def view_questions():
    line()
    print("  ALL QUESTIONS")
    line()
    if len(questions) == 0:
        print("  No questions.")
        return
    for i in range(len(questions)):
        q = questions[i]
        print(f"\n  Q{i+1}. [{q['subject']}] {q['question']}")
        for key in q["choices"]:
            print(f"     {key}) {q['choices'][key]}")
        print(f"     Correct: {q['answer']}")

def add_question():
    line()
    print("  ADD QUESTION")
    line()
    subj = input("Subject: ").strip()
    qtext = input("Question: ").strip()
    a = input("Choice A: ").strip()
    b = input("Choice B: ").strip()
    c = input("Choice C: ").strip()
    d = input("Choice D: ").strip()
    ans = ""
    while ans not in ["A", "B", "C", "D"]:
        ans = input("Correct Answer (A/B/C/D): ").strip().upper()
    questions.append({"subject": subj, "question": qtext, "choices": {"A": a, "B": b, "C": c, "D": d}, "answer": ans})
    print(f"  Added! Total questions: {len(questions)}")

def delete_question():
    line()
    print("  DELETE QUESTION")
    line()
    if len(questions) == 0:
        print("  No questions to delete.")
        return
    for i in range(len(questions)):
        print(f"  {i+1}. {questions[i]['question']}")
    num = input("Enter number to delete (0 to cancel): ").strip()
    if num == "0":
        return
    if num.isdigit():
        idx = int(num) - 1
        if 0 <= idx < len(questions):
            removed = questions.pop(idx)
            print(f"  Deleted: {removed['question']}")
        else:
            print("  Invalid number.")

def bank_stats():
    line()
    print(f"  Total Questions: {len(questions)}")
    counts = {}
    for q in questions:
        s = q["subject"]
        if s in counts:
            counts[s] = counts[s] + 1
        else:
            counts[s] = 1
    for s in counts:
        print(f"  {s}: {counts[s]}")

def view_all_results():
    line()
    print("  ALL STUDENT RESULTS")
    line()
    if len(all_results) == 0:
        print("  No results yet.")
        return
    for i in range(len(all_results)):
        r = all_results[i]
        print(f"  {i+1}. {r['name']} | Roll: {r['roll']} | Score: {r['score']} | {r['percentage']}% | {r['grade']}")

def view_one_result():
    view_all_results()
    if len(all_results) == 0:
        return
    num = input("Enter result number to view (0 to cancel): ").strip()
    if num == "0":
        return
    if num.isdigit():
        idx = int(num) - 1
        if 0 <= idx < len(all_results):
            r = all_results[idx]
            line()
            print(f"  {r['name']} | {r['roll']} | {r['score']} pts | {r['percentage']}% | {r['grade']}")
            print()
            for item in r["review"]:
                print(f"  Q{item['number']}. {item['question']}")
                print(f"     Your: {item['given']}  |  Correct: {item['correct']}  |  {item['result']}")

def class_stats():
    line()
    if len(all_results) == 0:
        print("  No results yet.")
        return
    scores = []
    for r in all_results:
        scores.append(r["score"])
    high = scores[0]
    low = scores[0]
    total = 0
    for s in scores:
        if s > high: high = s
        if s < low: low = s
        total = total + s
    avg = total / len(scores)
    passed = 0
    failed = 0
    for r in all_results:
        if r["percentage"] >= 50:
            passed = passed + 1
        else:
            failed = failed + 1
    print(f"  Total: {len(all_results)}  |  High: {high}  |  Low: {low}  |  Avg: {round(avg,1)}")
    print(f"  Passed: {passed}  |  Failed: {failed}")

def admin_portal():
    if not login(ADMIN_USER, ADMIN_PASS, "ADMIN PORTAL"):
        return
    while True:
        line()
        print("  ADMIN MENU")
        line()
        print("  1. View All Questions")
        print("  2. Add Question")
        print("  3. Delete Question")
        print("  4. Question Bank Stats")
        print("  5. View All Results")
        print("  6. View One Result")
        print("  7. Class Stats")
        print("  8. Logout")
        line()
        c = input("Choice (1-8): ").strip()
        if c == "1": view_questions()
        elif c == "2": add_question()
        elif c == "3": delete_question()
        elif c == "4": bank_stats()
        elif c == "5": view_all_results()
        elif c == "6": view_one_result()
        elif c == "7": class_stats()
        elif c == "8":
            print("  Logged out.")
            break
        else:
            print("  Invalid choice.")
        input("\n  Press Enter to continue...")

# ---- STUDENT FUNCTIONS ----

def show_rules():
    line()
    print("  EXAM RULES")
    line()
    print("  A/B/C/D = answer  |  S = skip  |  SUBMIT = end early")
    print("  Correct: +4  |  Wrong: -1  |  Skip: 0")
    print("  80%+ = EXCELLENT  |  65%+ = GOOD  |  50%+ = AVERAGE  |  <50% = BELOW AVERAGE")

def start_exam(name, roll):
    line()
    print(f"  EXAM STARTED  |  {name}  |  {roll}  |  {len(questions)} questions")
    line()
    answers = {}
    exam_time = time.strftime("%d-%b-%Y %I:%M %p")

    for i in range(len(questions)):
        q = questions[i]
        print(f"\n  Q{i+1}/{len(questions)}  [{q['subject']}]  {q['question']}")
        for key in q["choices"]:
            print(f"    {key}) {q['choices'][key]}")
        while True:
            ans = input("  Answer: ").strip().upper()
            if ans in ["A", "B", "C", "D", "S"]:
                answers[i] = ans
                break
            elif ans == "SUBMIT":
                for j in range(i, len(questions)):
                    answers[j] = "S"
                print("  Exam submitted early.")
                show_result(name, roll, answers, exam_time)
                return
            else:
                print("  Enter A, B, C, D, S, or SUBMIT.")

    print("  All done. Auto-submitted.")
    show_result(name, roll, answers, exam_time)

def show_result(name, roll, answers, exam_time):
    correct = 0
    wrong = 0
    skipped = 0
    review = []

    for i in range(len(questions)):
        q = questions[i]
        given = answers.get(i, "S")
        correct_ans = q["answer"]
        if given == "S":
            result_text = "Skipped"
            skipped = skipped + 1
        elif given == correct_ans:
            result_text = "Correct"
            correct = correct + 1
        else:
            result_text = "Wrong (Correct: " + correct_ans + ")"
            wrong = wrong + 1
        review.append({"number": i+1, "question": q["question"], "given": given, "correct": correct_ans, "result": result_text})

    max_score = len(questions) * 4
    score = (correct * 4) + (wrong * -1)
    percentage = round((score / max_score) * 100, 2)
    g = grade(percentage)

    line()
    print(f"  {name}  |  {roll}  |  {exam_time}")
    print(f"  Correct: {correct}  Wrong: {wrong}  Skipped: {skipped}")
    print(f"  Score: {score}/{max_score}  |  {percentage}%  |  {g}")
    line()
    print("  REVIEW:")
    for item in review:
        print(f"  Q{item['number']}. {item['question']}")
        print(f"     Your: {item['given']}  Correct: {item['correct']}  -> {item['result']}")

    all_results.append({"name": name, "roll": roll, "score": score, "percentage": percentage, "grade": g, "time": exam_time, "review": review})

def student_portal():
    if not login(STU_USER, STU_PASS, "STUDENT PORTAL"):
        return
    name = input("  Your Full Name: ").strip()
    roll = input("  Your Roll Number: ").strip()
    while True:
        line()
        print(f"  STUDENT MENU  |  Welcome {name}!")
        line()
        print("  1. Exam Rules")
        print("  2. Start Exam")
        print("  3. Logout")
        line()
        c = input("Choice (1-3): ").strip()
        if c == "1": show_rules()
        elif c == "2": start_exam(name, roll)
        elif c == "3":
            print(f"  Goodbye {name}!")
            break
        else:
            print("  Invalid choice.")
        input("\n  Press Enter to continue...")

# ---- MAIN ----

while True:
    line()
    print("  ECAT EXAM APP  |  CMPE-112L  |  UET Lahore")
    line()
    print("  1. Admin Portal")
    print("  2. Student Portal")
    print("  3. Exit")
    line()
    c = input("Select (1-3): ").strip()
    if c == "1": admin_portal()
    elif c == "2": student_portal()
    elif c == "3":
        print("  Goodbye!")
        break
    else:
        print("  Invalid choice.")