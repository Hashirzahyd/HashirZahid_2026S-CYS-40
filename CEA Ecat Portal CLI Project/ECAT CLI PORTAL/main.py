# ECAT Exam App | CMPE-112L | UET Lahore
# Hashir Zahid, 2026(S)-CYS-40 

ADMIN_USER = "ecat_admin"
ADMIN_PASS = "ecat@2026"
STU_USER = "student"
STU_PASS = "student123"

questions = [
    {"subject": "Physics",     "q": "SI unit of force?",                     "A": "Joule",    "B": "Newton",    "C": "Watt",     "D": "Pascal",   "ans": "B"},
    {"subject": "Chemistry",   "q": "Chemical formula of water?",            "A": "H2O2",     "B": "CO2",       "C": "H2O",      "D": "NaCl",     "ans": "C"},
    {"subject": "Mathematics", "q": "Value of pi (approx)?",                 "A": "3.14",     "B": "2.71",      "C": "1.41",     "D": "1.73",     "ans": "A"},
    {"subject": "Physics",     "q": "Speed of light in vacuum?",             "A": "3x10^6",   "B": "3x10^8",   "C": "3x10^10",  "D": "3x10^4",   "ans": "B"},
    {"subject": "Chemistry",   "q": "Most abundant gas in atmosphere?",      "A": "Oxygen",   "B": "CO2",       "C": "Hydrogen", "D": "Nitrogen", "ans": "D"},
    {"subject": "Mathematics", "q": "Square root of 144?",                   "A": "11",       "B": "12",        "C": "13",       "D": "14",       "ans": "B"},
    {"subject": "Physics",     "q": "Action-reaction is Newton's...?",       "A": "1st Law",  "B": "2nd Law",   "C": "3rd Law",  "D": "Hooke's",  "ans": "C"},
    {"subject": "Chemistry",   "q": "Atomic number of Carbon?",              "A": "4",        "B": "6",         "C": "8",        "D": "12",       "ans": "B"},
    {"subject": "Mathematics", "q": "15% of 200?",                           "A": "25",       "B": "30",        "C": "35",       "D": "40",       "ans": "B"},
    {"subject": "Physics",     "q": "Energy of a moving object?",            "A": "Potential","B": "Chemical",  "C": "Kinetic",  "D": "Nuclear",  "ans": "C"},
    {"subject": "Chemistry",   "q": "pH of pure water?",                     "A": "5",        "B": "6",         "C": "7",        "D": "8",        "ans": "C"},
    {"subject": "Mathematics", "q": "Degrees in a right angle?",             "A": "45",       "B": "60",        "C": "90",       "D": "180",      "ans": "C"},
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
    for attempt in range(3):
        u = input("Username: ").strip()
        p = input("Password: ").strip()
        if u == user and p == passw:
            print("  Login successful!")
            return True
        left = 2 - attempt
        if left > 0:
            print(f"  Wrong! {left} attempt(s) left.")
        else:
            print("  Access locked.")
    return False

# ---- ADMIN ----

def view_questions():
    line()
    print("  ALL QUESTIONS")
    line()
    if not questions:
        print("  No questions.")
        return
    for i, q in enumerate(questions):
        print(f"\n  Q{i+1}. [{q['subject']}] {q['q']}")
        for k in ["A", "B", "C", "D"]:
            print(f"     {k}) {q[k]}")
        print(f"     Correct: {q['ans']}")

def add_question():
    line()
    print("  ADD QUESTION")
    line()
    new = {}
    new["subject"] = input("Subject: ").strip()
    new["q"] = input("Question: ").strip()
    for k in ["A", "B", "C", "D"]:
        new[k] = input(f"Choice {k}: ").strip()
    new["ans"] = ""
    while new["ans"] not in ["A", "B", "C", "D"]:
        new["ans"] = input("Correct Answer (A/B/C/D): ").strip().upper()
    questions.append(new)
    print(f"  Added! Total: {len(questions)}")

def delete_question():
    line()
    print("  DELETE QUESTION")
    line()
    if not questions:
        print("  No questions.")
        return
    for i, q in enumerate(questions):
        print(f"  {i+1}. {q['q']}")
    num = input("Enter number to delete (0 to cancel): ").strip()
    if num == "0":
        return
    if num.isdigit() and 0 <= int(num)-1 < len(questions):
        removed = questions.pop(int(num)-1)
        print(f"  Deleted: {removed['q']}")
    else:
        print("  Invalid number.")

def view_all_results():
    line()
    print("  ALL RESULTS")
    line()
    if not all_results:
        print("  No results yet.")
        return
    for i, r in enumerate(all_results):
        print(f"  {i+1}. {r['name']} | {r['roll']} | Score: {r['score']} | {r['pct']}% | {r['grade']}")

def class_stats():
    line()
    if not all_results:
        print("  No results yet.")
        return
    scores = [r["score"] for r in all_results]
    avg = round(sum(scores) / len(scores), 1)
    passed = sum(1 for r in all_results if r["pct"] >= 50)
    print(f"  Total: {len(all_results)} | High: {max(scores)} | Low: {min(scores)} | Avg: {avg}")
    print(f"  Passed: {passed} | Failed: {len(all_results) - passed}")

def bank_stats():
    line()
    print("  QUESTION BANK STATS")
    line()
    print(f"  Total Questions : {len(questions)}")
    counts = {}
    for q in questions:
        s = q["subject"]
        counts[s] = counts.get(s, 0) + 1
    for s, c in counts.items():
        print(f"  {s:<15}: {c} question(s)")
    answers = [q["ans"] for q in questions]
    for k in ["A", "B", "C", "D"]:
        print(f"  Correct = {k}    : {answers.count(k)} question(s)")

def admin_portal():
    if not login(ADMIN_USER, ADMIN_PASS, "ADMIN PORTAL"):
        return
    while True:
        line()
        print("  ADMIN MENU")
        line()
        print("  1. View Questions\n  2. Add Question\n  3. Delete Question")
        print("  4. Bank Stats\n  5. View Results\n  6. Class Stats\n  7. Logout")
        line()
        c = input("Choice (1-7): ").strip()
        if   c == "1": view_questions()
        elif c == "2": add_question()
        elif c == "3": delete_question()
        elif c == "4": bank_stats()
        elif c == "5": view_all_results()
        elif c == "6": class_stats()
        elif c == "7":
            print("  Logged out.")
            break
        else:
            print("  Invalid choice.")
        input("\n  Press Enter to continue...")

# ---- STUDENT ----

def start_exam(name, roll):
    line()
    print(f"  EXAM | {name} | {roll} | {len(questions)} questions")
    print("  A/B/C/D = answer | S = skip | SUBMIT = end early")
    print("  Correct +4 | Wrong -1 | Skip 0")
    line()

    answers = {}
    for i, q in enumerate(questions):
        print(f"\n  Q{i+1}/{len(questions)} [{q['subject']}] {q['q']}")
        for k in ["A", "B", "C", "D"]:
            print(f"    {k}) {q[k]}")
        while True:
            ans = input("  Answer: ").strip().upper()
            if ans in ["A", "B", "C", "D", "S"]:
                answers[i] = ans
                break
            elif ans == "SUBMIT":
                for j in range(i, len(questions)):
                    answers[j] = "S"
                print("  Submitted early.")
                show_result(name, roll, answers)
                return
            else:
                print("  Enter A, B, C, D, S, or SUBMIT.")

    show_result(name, roll, answers)

def show_result(name, roll, answers):
    correct = wrong = skipped = 0
    review = []

    for i, q in enumerate(questions):
        given = answers.get(i, "S")
        if given == "S":
            result = "Skipped"
            skipped += 1
        elif given == q["ans"]:
            result = "Correct"
            correct += 1
        else:
            result = f"Wrong (Correct: {q['ans']})"
            wrong += 1
        review.append({"num": i+1, "q": q["q"], "given": given, "correct": q["ans"], "result": result})

    max_score = len(questions) * 4
    score = correct * 4 - wrong
    pct = round((score / max_score) * 100, 2)
    g = grade(pct)

    line()
    print(f"  {name} | {roll}")
    print(f"  Correct: {correct} | Wrong: {wrong} | Skipped: {skipped}")
    print(f"  Score: {score}/{max_score} | {pct}% | {g}")
    line()
    print("  REVIEW:")
    for item in review:
        print(f"  Q{item['num']}. {item['q']}")
        print(f"     Your: {item['given']} | Correct: {item['correct']} | {item['result']}")

    all_results.append({"name": name, "roll": roll, "score": score, "pct": pct, "grade": g, "review": review})

def student_portal():
    if not login(STU_USER, STU_PASS, "STUDENT PORTAL"):
        return
    name = input("  Your Full Name: ").strip()
    roll = input("  Your Roll Number: ").strip()
    while True:
        line()
        print(f"  STUDENT MENU | Welcome {name}!")
        line()
        print("  1. Start Exam\n  2. Logout")
        line()
        c = input("Choice (1-2): ").strip()
        if c == "1": start_exam(name, roll)
        elif c == "2":
            print(f"  Goodbye {name}!")
            break
        else:
            print("  Invalid choice.")
        input("\n  Press Enter to continue...")

# ---- MAIN ----

while True:
    line()
    print("  ECAT EXAM APP | CMPE-112L | UET Lahore")
    line()
    print("  1. Admin Portal\n  2. Student Portal\n  3. Exit")
    line()
    c = input("Select (1-3): ").strip()
    if c == "1": admin_portal()
    elif c == "2": student_portal()
    elif c == "3":
        print("  Goodbye!")
        break
    else:
        print("  Invalid choice.")
