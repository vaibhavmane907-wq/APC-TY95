with open("sample.txt", "w") as file:
    file.write("Hello world\n")
    file.write("Python is easy\n")
    file.write("I am learning Python")


with open("sample.txt", "r") as file:
    text = file.read()


lines = len(text.splitlines())
words = len(text.split())
characters = len(text)


print("Lines:", lines)
print("Words:", words)
print("Characters:", characters)