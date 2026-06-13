with open("Practice.txt", "r") as f:
    '''f.write("Hi everyone\n we are learning Pythone\n")
    f.write("using Java\n I like programming in java")'''
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)