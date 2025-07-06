print("Hello! I'm a simple chatbot. Type 'quit' to end the conversation.")

while True:
    user_input = input("You: ").lower()
    
    if user_input == 'quit':
        print("Chatbot: Goodbye! Have a great day!")
        break
        
    elif 'hello' in user_input or 'hi' in user_input:
        print("Chatbot: Hi there! How can I help you?")
        
    elif 'how are you' in user_input:
        print("Chatbot: I'm just a program, but I'm functioning well! How about you?")
        
    elif 'your name' in user_input:
        print("Chatbot: I'm Chatbot 1.0. What's your name?")
        
    elif 'weather' in user_input:
        print("Chatbot: I'm not connected to weather services, but it's always sunny in the digital world!")
        
    elif 'thank' in user_input:
        print("Chatbot: You're welcome!")
        
    elif 'help' in user_input:
        print("Chatbot: I can respond to greetings, tell you about myself, and more. Try asking simple questions!")
        
    elif 'joke' in user_input:
        print("Chatbot: Why don't scientists trust atoms? Because they make up everything!")
        
    elif 'time' in user_input:
        print("Chatbot: I don't have access to the current time. Maybe check your device?")
        
    elif '?' in user_input:
        print("Chatbot: That's an interesting question. Unfortunately, my knowledge is limited.")
        
    else:
        print("Chatbot: I'm not sure how to respond to that. Can you try asking something else?")