def first_and_last(message):
    if not message:
        return True
    else:
        return message[0] == message[-1]
    
print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))