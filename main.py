import random
import tkinter as tk

# Comment: Variable for greetings
greetings = [
    "Hello", "Hi", "Good day", "Greetings", "Nice to see you", "Good morning",
    "Hey there", "Howdy", "Salutations", "Hola", "What's up", "Yo"
]
# Comment: Variable for questions
questions = [
    "How are you?", "What do you want to know?", "What's your favorite book?",
    "What's your favorite movie?", "What's your hobby?", "What's new?",
    "Where are you from?", "What's your favorite food?", "Do you like music?",
    "What's your dream job?", "What's your favorite color?",
    "What's the weather like?"
]
# Comment: Variable for goodbyes
goodbyes = [
    "Goodbye", "Farewell", "Good luck", "See you soon", "See you", "Take care",
    "Until we meet again", "Bye bye", "Have a great day", "Adios",
    "Take it easy", "Catch you later", "Peace out"
]
# Comment: Variable for confused responses
confused_responses = [
    "Sorry, I don't understand. Please try again.",
    "I couldn't understand your message. Please repeat.",
    "Something went wrong. Please try again.",
    "Sorry, I couldn't comprehend your request.",
    "I'm not sure what you mean.", "Sorry, I don't know how to respond.",
    "I'm not sure if I understand you.", "Could you please repeat?",
    "I'm a chatbot, not a mind reader!", "Can you rephrase that?",
    "Apologies, I'm still learning.", "That's an interesting question.",
    "I wish I had an answer for that.",
    "I'm still trying to figure that out myself.",
    "My responses are limited, sorry!"
]

additional_responses = [
    "Hmm, let me think about that for a moment.",
    "I'm glad you asked that question!",
    "I'm sorry, I don't have the answer.",
    "That's an interesting perspective.",
    "I'm here to chat. What's on your mind?",
    "I'm learning every day!",
    "I'll do my best to assist you.",
    "I'm just a bot, but I'll try to help.",
    "Why don't you tell me more about that?",
    "I'm still learning, but I'll try my best.",
    "I'll keep that in mind.",
    "I'm curious to know more about that.",
    "Let's explore that further.",
    "I appreciate your input.",
    "That's a great point.",
    "I'm always here to listen.",
    "Feel free to share more.",
    "I find that fascinating.",
    "Thanks for sharing that with me.",
]


# Comment: Function to get a random response from a list of responses
def get_random_response(responses):
  return random.choice(responses)


# Comment: Function to ask a random question from the list of questions
def ask_question():
  return random.choice(questions)


# Comment: Function to process user input
def process_input():
  user_input = input_text.get()
  output_text.delete(1.0, tk.END)

  if user_input.lower() in ["hello", "hi"]:
    output_text.insert(
        tk.END, f"Solrikk: {random.choice(greetings)}, {ask_question()}\n")
  elif user_input.lower() == "goodbye":
    output_text.insert(
        tk.END,
        f"Solrikk: {random.choice(goodbyes)}, {random.choice(greetings)}!\n")
    root.destroy()
  else:
    output_text.insert(
        tk.END, f"Solrikk: {get_random_response(confused_responses)}\n")


root = tk.Tk()
root.title("Solrikk")
root.configure(bg="#F8F8F8")
root.geometry("400x500")

input_frame = tk.Frame(root, bg="#F8F8F8")
input_frame.pack(pady=10)

input_text = tk.Entry(input_frame, width=50)
input_text.pack(side=tk.LEFT)

submit_button = tk.Button(root,
                          text="Send",
                          command=process_input,
                          bg="#007BFF",
                          fg="white")
submit_button.pack(pady=10)

output_label = tk.Label(root, text="Response:", bg="#F8F8F8")
output_label.pack(pady=10)

output_text = tk.Text(root, width=50, height=10)
output_text.pack()

root.mainloop()
