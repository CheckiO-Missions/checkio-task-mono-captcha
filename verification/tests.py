"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {"input": [[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                   [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                   [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                   [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                   [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]],
         "answer": 394,
         "explanation": ""},
        {"input": [[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
                   [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                   [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                   [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                   [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]],
         "answer": 394,
         "explanation": " 3,1 3,5 0,10 "},
    ],
    "Clear": [
        {"input": [[0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                   [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                   [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
                   [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0]],
         "answer": 123,
         "explanation": ""},

        {"input": [[0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
                   [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                   [0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0],
                   [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                   [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0]],
         "answer": 456,
         "explanation": ""},

        {"input": [[0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
                   [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                   [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                   [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                   [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0]],
         "answer": 789,
         "explanation": ""},

        {"input": [[0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0],
                   [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                   [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0],
                   [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                   [0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0]],
         "answer": 1034,
         "explanation": ""},

        {"input": [[0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                   [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                   [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0],
                   [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
                   [0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0]],
         "answer": 52678,
         "explanation": ""},

        {"input": [[0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                   [0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0],
                   [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                   [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]],
         "answer": 911,
         "explanation": ""},

        {"input": [[0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                   [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                   [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                   [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                   [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]],
         "answer": 777,
         "explanation": ""},

        {"input": [[0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0],
                   [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
                   [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
                   [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                   [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0]],
         "answer": 21312,
         "explanation": ""},

        {"input": [[0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0],
                   [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                   [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
                   [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                   [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0]],
         "answer": 80808,
         "explanation": ""},
    ],
    "Noise": [
        {"input": [[0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                   [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                   [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0],
                   [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0]],
         "answer": 123,
         "explanation": " 1,3 1,5 2,11 "},

        {"input": [[0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
                   [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                   [0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0],
                   [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                   [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0]],
         "answer": 456,
         "explanation": " 4,2 3,5 3,9 "},

        {"input": [[0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
                   [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
                   [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0],
                   [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                   [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0]],
         "answer": 789,
         "explanation": " 2,2 2,6 1,10 "},

        {"input": [[0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0],
                   [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                   [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
                   [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                   [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0]],
         "answer": 1034,
         "explanation": " 1,1 4,7 1,10 2,14 "},

        {"input": [[0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                   [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                   [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0],
                   [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                   [0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0]],
         "answer": 52678,
         "explanation": " 2,1 2,5 1,9 3,15 2,17 "},

        {"input": [[0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0],
                   [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                   [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]],
         "answer": 911,
         "explanation": " 4,1 4,6 0,10 "},

        {"input": [[0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                   [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                   [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
                   [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                   [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]],
         "answer": 777,
         "explanation":  " 1,2 1,5 2,9 "},

        {"input": [[0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
                   [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
                   [0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                   [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0]],
         "answer": 21312,
         "explanation": " 3,3 3,5 0,11 1,14 4,17 "},

        {"input": [[0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                   [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                   [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                   [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                   [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0]],
         "answer": 80808,
         "explanation": " 1,2 4,5 3,10 0,15 2,18 "},
    ]
}
