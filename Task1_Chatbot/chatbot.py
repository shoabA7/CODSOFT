print("MAX BOT started (type bye to exit)\n")

name = input("Enter your name: ")
print("Welcome", name)

while True:
    user = input(name + ": ").lower().strip()

    if user == "hi" or user == "hello":
        print("Max Bot: Hello! how can I help you")
    
    elif user == "hii" or user == "hlo":
        print("Max Bot: Hi there!")
    
    elif "how are you" in user:
        print("Max Bot: I am good, what about you?")
    
    elif "your name" in user:
        print("Max Bot: I am Max Bot created using python")
    
    elif "college" in user:
        print("Max Bot: I study at Dhanekula Institute")
    
    elif "internship" in user:
        print("Max Bot: I am doing internship at CodSoft")
    
    elif "skill" in user:
        print("Max Bot: I am learning python and web development")
    
    elif "project" in user:
        print("Max Bot: I created this chatbot using if else")
    
    elif "goal" in user:
        print("Max Bot: My goal is to become software developer")
    
    elif user == "bye":
        print("Max Bot: okay bye!")
        break
    
    else:
        print("Max Bot: not sure, try simple words")