from ai import ask_ai

while True:
    question = input("Ask Jarvis: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    print("\nJarvis:\n")
    print(ask_ai(question))
    print()