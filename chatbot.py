import datetime

def save_message(sender, message):
    """you save every message in file history.txt"""

    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(f"[{time}] {sender}: {memory}\n")

#------------------------------------------------------------------------
# display function
def display_welcome():
    """print the Welcome message when the program starts"""

    print("="* 40)
    print(" Welcome to DecodeLabs Chatbot")
    print(" Type 'exit' to quit.")
    print("="* 40)


def display_farewell():
    """print the Farewell message when the program ends"""

    print("="* 40)
    print(" Thanks for chatting! Goodbye")
    print("="* 40)

#-----------------------------------------------------------------
# input handling

def get_user_input():
    """it takes input from the user and returns it clean (lowercase + strip)"""

    raw = input("\nYou: ")
    return raw.lower().strip()

#-----------------------------------------------------------------------
# response logic

RESPONSES = {
    "hello":           "Hey there! How can I help you?",
    "hi":              "Hey there! How can I help you?",
    "how are you":     "I'm just a bot, but running perfectly!",
    "what is your name": "I'm DecoBot - your AI assistant!",
    "what can you do": "I answer questions. More features coming soon!",
    "bye":             "Goodbye! It was nice talking to you.",
    "goodbye":         "Goodbye! It was nice talking to you.",
}

KEYWORDS = {
    "hello":  "Hey there! How can I help you?",
    "hi":     "Hey there! How can I help you?",
    "help":   "Sure! I'm here to help you.",
    "name":   "I'm DecoBot - your AI assistant!",
    "do":     "I answer questions. More features coming soon!",
    "bye":    "Goodbye! It was nice talking to you.",
    "good":   "I'm doing great, thanks for asking!",
}

def keyword_match(user_input):
    """search for any ketword in the sentence and returns the correct response"""

    for keyword in KEYWORDS:
        if keyword in user_input:
            return KEYWORDS[keyword]
    return None

def get_response(user_input):

    update_memory(user_input)

    memory_response = get_memory_response(user_input)
    if memory_response:
        return memory_response
    

    if user_input in RESPONSES:
        return RESPONSES[user_input]
    

    keyword_response = keyword_match(user_input)
    if keyword_response:
        return keyword_response
    

    return "I didn't understand. Try:hello / how are you / bye"
    
#-------------------------------------------------------------------------
# memory

memory ={
    "name":None
}

def update_memory(user_input):
    """search for information in input and saved it in memory"""

    words = user_input.split()


    if "my name is" in user_input:
        name_index = words.index("is") + 1
        if name_index < len(words):
            memory["name"]=words[name_index].capitalize()



def get_memory_response(user_input):
    """you checks if the question requires memory and returns a response"""


    if "what is my name" in user_input or "my name" in user_input and "is" not in user_input:
        if memory["name"]:
            return f"Your name is {memory['name']}!"
        else:
            return "I don't know your name yet! Tell me: my name is ..."
        

    if "my name is" in user_input:
        if memory["name"]:
            return f"Nice to meet you, {memory['name']}!"
        

    return None

#------------------------------------------------------------------------------------------------------------
# main loop

def run_chatbot():
    """Main function that runs the chatbot loop. it gathers all the functions together"""

    display_welcome()

    while True:

        user_input = get_user_input()

        if user_input == "exit":
            save_message("System", "Session ended")
            display_farewell()
            break

        save_message("You", user_input)

        response = get_response(user_input)
        print(f"Bot: {response}")


        save_message("Bot", response)

#------------------------------------------------------------------------------
# entry point

def main():
    run_chatbot()


if __name__ =="__main__":
    main()

