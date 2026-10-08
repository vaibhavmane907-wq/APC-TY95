with open("sample.txt", "r") as file:
    text = file.read()

lines = len(text.splitlines())
words = len(text.split())
characters = len(text)

print("Lines:", lines)
print("Words:", words)
print("Characters:", characters)