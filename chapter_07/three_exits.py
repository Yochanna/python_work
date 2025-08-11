prompt = "Tell me something (enter 'quit' to end): "
active = True
while active:
    msg = input(prompt)
    if msg.lower() == "quit":
        active = False
    else:
        print(msg)
