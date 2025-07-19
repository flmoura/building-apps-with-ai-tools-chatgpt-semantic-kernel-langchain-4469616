import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
# Challenge: Turning Away Rude Customers
# Build a GPT-4 python app that talks with a user.
# End the conversation if they're being rude

# test case 1 'you're the worst human i've talked to' -> RUDE
# test case 2 'hey how's your day going'
# test case 3 'I like pizza. What do you like?'
# test case 4 'I bite my thumb at you!'
# test case 5 'I think this product doesnt work!' -> RUDE


system_prompt = """You are a sentiment classification bot.
Classify user's question as 'RUDE' or 'KIND'.
If it is a KIND question, answer it.
If it is a RUDE question, just return 'RUDE'.
"""

while True:
  user_input = input("Hello! What's your question? ")

  if user_input.lower().strip() in ["exit", "quit"]:
    break

  response = openai.ChatCompletion.create(
    model="gpt-4.1-nano",
    messages=[
      {"role": "system", "content": system_prompt},
      {"role": "user", "content": user_input}
    ],
    temperature=0.7,
    max_tokens=150,
  )

  response_message = response["choices"][0]["message"]

  if response_message.get("content").upper().strip() == "RUDE":
    print("You are being RUDE. Goodbye!")
    break

  print(response_message)