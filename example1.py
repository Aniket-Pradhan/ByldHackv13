user = "b2aca159-86a0-4afa-9b22-4b720ee1957f"
passwd = "vTSl6VKjZMPA"

from watson import watson_run
from test2 import parse

cmd = ["assign variable b with six",
"assign variable a with five",
"create for loop of variable i from one to two",
"create if variable b greater than variable a",
"assign variable a with variable a plus variable b",
"done",
"create else",
"assign variable a with variable a minus variable b",
"done",
"create while not variable a less than or equals variable b and variable c not equals seven",
"function variable a",
"assign variable a with variable a minus one",
"done",
"done"
]

for i in cmd:
    parse(i)