from app import create_app, db
from app.models import Subject, Chapter, Quiz, Question, Admin, User, Score
from datetime import date

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    subjects_data = {
            "Python": {
                "Basics": [
                    {
                        "question": "What is the correct file extension for Python files?",
                        "options": ["A. .py", "B. .pt", "C. .pyt", "D. .python"],
                        "answer": "A"
                    },
                    {
                        "question": "Which keyword is used for function in Python?",
                        "options": ["A. fun", "B. define", "C. function", "D. def"],
                        "answer": "D"
                    },
                    {
                        "question": "How do you insert COMMENTS in Python code?",
                        "options": ["A. //comment", "B. #comment", "C. /*comment*/", "D. <!--comment-->"],
                        "answer": "B"
                    },
                    {
                        "question": "What is the output of: print(2 ** 3)?",
                        "options": ["A. 6", "B. 8", "C. 9", "D. 5"],
                        "answer": "B"
                    },
                    {
                        "question": "What is the correct way to create a variable?",
                        "options": ["A. x = 5", "B. int x = 5", "C. declare x = 5", "D. 5 -> x"],
                        "answer": "A"
                    },
                    {
                        "question": "Which data type is immutable?",
                        "options": ["A. List", "B. Set", "C. Dictionary", "D. Tuple"],
                        "answer": "D"
                    },
                    {
                        "question": "What is the output of: len('hello')?",
                        "options": ["A. 4", "B. 5", "C. 6", "D. Error"],
                        "answer": "B"
                    },
                    {
                        "question": "What is used to handle exceptions?",
                        "options": ["A. try/except", "B. catch/throw", "C. if/else", "D. do/catch"],
                        "answer": "A"
                    },
                    {
                        "question": "How do you define a list?",
                        "options": ["A. {1,2,3}", "B. [1,2,3]", "C. (1,2,3)", "D. <1,2,3>"],
                        "answer": "B"
                    },
                    {
                        "question": "Which of the following is not a keyword?",
                        "options": ["A. True", "B. None", "C. eval", "D. while"],
                        "answer": "C"
                    },
                ],
                "Control Flow": [
                    {
                        "question": "Which keyword starts a loop in Python?",
                        "options": ["A. for", "B. repeat", "C. loop", "D. while"],
                        "answer": "A"
                    },
                    {
                        "question": "What is the output: print(range(3))?",
                        "options": ["A. [0, 1, 2]", "B. range(3)", "C. 3", "D. Error"],
                        "answer": "B"
                    },
                    {
                        "question": "What breaks out of a loop?",
                        "options": ["A. end", "B. stop", "C. break", "D. exit"],
                        "answer": "C"
                    },
                    {
                        "question": "What continues to the next iteration?",
                        "options": ["A. jump", "B. skip", "C. next", "D. continue"],
                        "answer": "D"
                    },
                    {
                        "question": "What is used to test multiple conditions?",
                        "options": ["A. for", "B. elif", "C. else if", "D. switch"],
                        "answer": "B"
                    },
                    {
                        "question": "Which of the following is a comparison operator?",
                        "options": ["A. =", "B. !", "C. !=", "D. <>"],
                        "answer": "C"
                    },
                    {
                        "question": "Which of these is not a logical operator?",
                        "options": ["A. and", "B. or", "C. not", "D. nor"],
                        "answer": "D"
                    },
                    {
                        "question": "What does 'pass' do?",
                        "options": ["A. Skips error", "B. Skips block", "C. Does nothing", "D. Loops again"],
                        "answer": "C"
                    },
                    {
                        "question": "Which loop runs at least once?",
                        "options": ["A. while", "B. for", "C. do-while", "D. repeat"],
                        "answer": "C"
                    },
                    {
                        "question": "How to iterate through a list?",
                        "options": ["A. for i in list", "B. list.for", "C. loop(list)", "D. foreach(list)"],
                        "answer": "A"
                    }
                ]
            },

            "Finance": {
                "Time Value": [
                    {
                        "question": "What is Time Value of Money?",
                        "options": ["A. Time is money", "B. Present is better than future", "C. Money loses value over time", "D. Value changes with inflation"],
                        "answer": "B"
                    },
                    {
                        "question": "What is FV?",
                        "options": ["A. Fund Value", "B. Final Value", "C. Future Value", "D. Fiscal Value"],
                        "answer": "C"
                    },
                    {
                        "question": "If interest is compounded annually, it is:",
                        "options": ["A. Simple interest", "B. Continuous", "C. Discrete", "D. Compounded"],
                        "answer": "D"
                    },
                    {
                        "question": "Present value is:",
                        "options": ["A. Future value + interest", "B. Future value - inflation", "C. Discounted future value", "D. Current bank balance"],
                        "answer": "C"
                    },
                    {
                        "question": "What increases FV?",
                        "options": ["A. Higher rate", "B. Lower time", "C. Lower rate", "D. No compounding"],
                        "answer": "A"
                    },
                    {
                        "question": "What is discounting?",
                        "options": ["A. Reducing cost", "B. Time travel", "C. Reverse compounding", "D. Giving discount"],
                        "answer": "C"
                    },
                    {
                        "question": "The formula for compound interest includes:",
                        "options": ["A. P*r*t", "B. P(1+rt)", "C. P(1+r)^t", "D. P+r+t"],
                        "answer": "C"
                    },
                    {
                        "question": "Which of these is not a time value tool?",
                        "options": ["A. FV", "B. PV", "C. CAGR", "D. ROE"],
                        "answer": "D"
                    },
                    {
                        "question": "Compounding frequency affects:",
                        "options": ["A. Tax", "B. Principal", "C. Returns", "D. None"],
                        "answer": "C"
                    },
                    {
                        "question": "What is annuity?",
                        "options": ["A. Lump sum", "B. Series of equal payments", "C. Future loan", "D. Profit"],
                        "answer": "B"
                    }
                ],
                "Valuation": [
                    {
                        "question": "Which model values companies based on dividends?",
                        "options": ["A. DCF", "B. DDM", "C. PE", "D. ROI"],
                        "answer": "B"
                    },
                    {
                        "question": "What is DCF?",
                        "options": ["A. Discount Cash Flows", "B. Direct Cash Finance", "C. Dollar Compounding Formula", "D. Debt Coverage Fund"],
                        "answer": "A"
                    },
                    {
                        "question": "What does PE ratio show?",
                        "options": ["A. Price/Earnings", "B. Profit Estimate", "C. Principal Equity", "D. Projected Earnings"],
                        "answer": "A"
                    },
                    {
                        "question": "Which is not a valuation method?",
                        "options": ["A. DCF", "B. Market cap", "C. Annuity", "D. PE"],
                        "answer": "C"
                    },
                    {
                        "question": "Which term shows book value?",
                        "options": ["A. Market value", "B. Intrinsic value", "C. Accounting value", "D. Fair value"],
                        "answer": "C"
                    },
                    {
                        "question": "Higher PE ratio usually means:",
                        "options": ["A. Overvaluation", "B. Undervaluation", "C. No value", "D. Dividends"],
                        "answer": "A"
                    },
                    {
                        "question": "Which sector has high PE usually?",
                        "options": ["A. IT", "B. FMCG", "C. Banking", "D. Energy"],
                        "answer": "A"
                    },
                    {
                        "question": "A company with no revenue can't be valued using:",
                        "options": ["A. DDM", "B. PE", "C. DCF", "D. All"],
                        "answer": "D"
                    },
                    {
                        "question": "What reduces company value?",
                        "options": ["A. High cash", "B. Growth", "C. High debt", "D. Brand"],
                        "answer": "C"
                    },
                    {
                        "question": "What is Beta in valuation?",
                        "options": ["A. Risk measure", "B. Return ratio", "C. Cost factor", "D. Profit"],
                        "answer": "A"
                    }
                ]
            },

                    "Statistics": {
                "Descriptive": [
                    {
                        "question": "What does mean represent?",
                        "options": ["A. Most frequent", "B. Middle value", "C. Average", "D. Total"],
                        "answer": "C"
                    },
                    {
                        "question": "Which is not a measure of central tendency?",
                        "options": ["A. Mode", "B. Mean", "C. Median", "D. Standard deviation"],
                        "answer": "D"
                    },
                    {
                        "question": "What does standard deviation show?",
                        "options": ["A. Spread", "B. Mean", "C. Shape", "D. Size"],
                        "answer": "A"
                    },
                    {
                        "question": "What is the median of [1, 3, 5, 7, 9]?",
                        "options": ["A. 5", "B. 6", "C. 4", "D. 3"],
                        "answer": "A"
                    },
                    {
                        "question": "What is the mode of [2, 2, 3, 4, 5]?",
                        "options": ["A. 3", "B. 2", "C. 4", "D. 5"],
                        "answer": "B"
                    },
                    {
                        "question": "Which graph shows frequency?",
                        "options": ["A. Histogram", "B. Line chart", "C. Scatter plot", "D. Pie chart"],
                        "answer": "A"
                    },
                    {
                        "question": "What does a boxplot show?",
                        "options": ["A. Mean", "B. Distribution", "C. Mode", "D. Total"],
                        "answer": "B"
                    },
                    {
                        "question": "Which is not affected by outliers?",
                        "options": ["A. Mean", "B. Median", "C. Range", "D. Standard deviation"],
                        "answer": "B"
                    },
                    {
                        "question": "What is range?",
                        "options": ["A. Max - Min", "B. Mean", "C. SD", "D. Mode"],
                        "answer": "A"
                    },
                    {
                        "question": "Which tool is used to summarize data?",
                        "options": ["A. Frequency table", "B. Histogram", "C. Mean", "D. Pie chart"],
                        "answer": "A"
                    }
                ],
                "Probability": [
                    {
                        "question": "Probability is always between:",
                        "options": ["A. 0 and 1", "B. -1 and 1", "C. 1 and 100", "D. 0 and ∞"],
                        "answer": "A"
                    },
                    {
                        "question": "Probability of a sure event is:",
                        "options": ["A. 0", "B. 1", "C. 0.5", "D. Can't say"],
                        "answer": "B"
                    },
                    {
                        "question": "What is the sum of probabilities of all outcomes?",
                        "options": ["A. 0", "B. 1", "C. ∞", "D. Depends"],
                        "answer": "B"
                    },
                    {
                        "question": "Probability of impossible event is:",
                        "options": ["A. 0", "B. 1", "C. -1", "D. ∞"],
                        "answer": "A"
                    },
                    {
                        "question": "Which distribution is symmetric?",
                        "options": ["A. Normal", "B. Binomial", "C. Poisson", "D. Exponential"],
                        "answer": "A"
                    },
                    {
                        "question": "What is used to calculate conditional probability?",
                        "options": ["A. Venn Diagram", "B. Tree Diagram", "C. Bayes Theorem", "D. Matrix"],
                        "answer": "C"
                    },
                    {
                        "question": "What is a sample space?",
                        "options": ["A. Area", "B. List of outcomes", "C. Formula", "D. Event"],
                        "answer": "B"
                    },
                    {
                        "question": "What is the probability of head in fair coin?",
                        "options": ["A. 0.25", "B. 0.75", "C. 0.5", "D. 1"],
                        "answer": "C"
                    },
                    {
                        "question": "Mutually exclusive events mean:",
                        "options": ["A. One or both", "B. Both together", "C. Never together", "D. At least one"],
                        "answer": "C"
                    },
                    {
                        "question": "Independent events mean:",
                        "options": ["A. Affect each other", "B. Can't happen", "C. No effect", "D. Mutually exclusive"],
                        "answer": "C"
                    }
                ]
            },

            "Computational Thinking": {
                "Patterns": [
                    {
                        "question": "What is pattern recognition?",
                        "options": ["A. Finding loops", "B. Finding similarities", "C. Finding bugs", "D. Debugging"],
                        "answer": "B"
                    },
                    {
                        "question": "Which of these is not a pattern?",
                        "options": ["A. Sequence", "B. Recursion", "C. Function", "D. Repetition"],
                        "answer": "C"
                    },
                    {
                        "question": "Which helps reduce complexity?",
                        "options": ["A. Breaking into patterns", "B. Increasing data", "C. Ignoring patterns", "D. None"],
                        "answer": "A"
                    },
                    {
                        "question": "What is abstraction?",
                        "options": ["A. Hiding details", "B. Adding data", "C. Ignoring input", "D. Showing everything"],
                        "answer": "A"
                    },
                    {
                        "question": "What is generalization?",
                        "options": ["A. Making code general", "B. Ignoring cases", "C. Copying code", "D. Specialization"],
                        "answer": "A"
                    },
                    {
                        "question": "Which problem has fixed pattern?",
                        "options": ["A. Sorting", "B. AI", "C. Painting", "D. Gaming"],
                        "answer": "A"
                    },
                    {
                        "question": "Finding repeated structures is called?",
                        "options": ["A. Looping", "B. Repetition", "C. Pattern recognition", "D. Matching"],
                        "answer": "C"
                    },
                    {
                        "question": "Why do we use patterns?",
                        "options": ["A. Save time", "B. Increase size", "C. Decrease logic", "D. Create errors"],
                        "answer": "A"
                    },
                    {
                        "question": "Which is a visual pattern?",
                        "options": ["A. Flowchart", "B. Algorithm", "C. Pseudocode", "D. Loop"],
                        "answer": "A"
                    },
                    {
                        "question": "Pattern recognition helps in:",
                        "options": ["A. Writing tests", "B. Identifying bugs", "C. Predicting solutions", "D. Guessing code"],
                        "answer": "C"
                    }
                ],
                "Algorithms": [
                    {
                        "question": "What is an algorithm?",
                        "options": ["A. Puzzle", "B. Game", "C. Step-by-step solution", "D. Pattern"],
                        "answer": "C"
                    },
                    {
                        "question": "Which is not a property of algorithm?",
                        "options": ["A. Input", "B. Output", "C. Accuracy", "D. Finiteness"],
                        "answer": "C"
                    },
                    {
                        "question": "What is a flowchart?",
                        "options": ["A. Graph", "B. Algorithm drawing", "C. Game", "D. Pattern"],
                        "answer": "B"
                    },
                    {
                        "question": "What does decision symbol represent?",
                        "options": ["A. Start", "B. Condition", "C. Loop", "D. End"],
                        "answer": "B"
                    },
                    {
                        "question": "Which is not a sorting algorithm?",
                        "options": ["A. Bubble", "B. Merge", "C. Insert", "D. Tree"],
                        "answer": "D"
                    },
                    {
                        "question": "Which is the fastest sorting?",
                        "options": ["A. Bubble", "B. Quick", "C. Insertion", "D. Selection"],
                        "answer": "B"
                    },
                    {
                        "question": "Why use algorithms?",
                        "options": ["A. Easy thinking", "B. Structured steps", "C. Fancy code", "D. Hard coding"],
                        "answer": "B"
                    },
                    {
                        "question": "What is the first step in algorithm design?",
                        "options": ["A. Code", "B. Understand problem", "C. Write loop", "D. Test"],
                        "answer": "B"
                    },
                    {
                        "question": "What does dry-run mean?",
                        "options": ["A. Write test", "B. Execute logic manually", "C. Print code", "D. Debug"],
                        "answer": "B"
                    },
                    {
                        "question": "Algorithm must terminate after:",
                        "options": ["A. A few lines", "B. Infinite steps", "C. Finite steps", "D. Any step"],
                        "answer": "C"
                    }
                ]
            }

        }

    for subject_name, chapters in subjects_data.items():
            subject = Subject(name=subject_name)
            db.session.add(subject)
            db.session.commit()

            for chapter_name, questions in chapters.items():
                chapter = Chapter(name=chapter_name, subject_id=subject.id)
                db.session.add(chapter)
                db.session.commit()

                quiz = Quiz(date=date(2025, 6, 25), duration="15 min", chapter_id=chapter.id)
                db.session.add(quiz)
                db.session.commit()

                for q in questions:
                    new_q = Question(
                        question_text=q["question"],
                        option_a=q["options"][0],
                        option_b=q["options"][1],
                        option_c=q["options"][2],
                        option_d=q["options"][3],
                        correct_answer=q["answer"],
                        quiz_id=quiz.id
                    )
                    db.session.add(new_q)

    db.session.commit()
    print("✔ Database created and seeded .")

