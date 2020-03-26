from Question import Question

question_prompts = [
  "What color are hippos?\n(a) Purple\n(b) Green\n(c) Red\n(d) Blue\n\n",
  "What color are lima beans?\n(a) Silver\n(b) Orange\n(c) Rainbow\n(d) Green\n\n",
  "What sound do turtles make?\n(a) 'Haha'\n(b) 'Nope'\n(c) 'I like Turtles'\n(d) All of the above\n\n"
]

questions = [
  Question(question_prompts[0], "a"),
  Question(question_prompts[1], "d"),
  Question(question_prompts[2], 'd')
]

def run_test(questions):
  score = 0
  for question in questions:
    answer = input(question.prompt)
    if answer == question.answer:
      score += 1
  print("You got " + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)