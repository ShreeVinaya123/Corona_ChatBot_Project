from Corona_ChatBot import predict_class, get_response

print("Start chatting with Corona ChatBot (type 'quit' to stop)")

while True:
    msg = input("You: ")
    if msg.lower() in ["quit", "exit", "bye"]:
        print("Bot: Goodbye! Stay safe.")
        break
    tag = predict_class(msg)
    reply = get_response(tag)
    print("Bot:", reply)
