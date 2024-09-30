from runner import run_conversation
from vars import INITIAL_MESSAGES

if __name__ == "__main__":
    print("""Welcome to SmarterLLM!
This program tries to make LLMs more intelligent by giving them access to the internet, the current date and time and making them better at math by using tools.\n
Enter a prompt (enter 'exit' to quit):""")

    while True:
        user_input = input(">>> ")
    
        if user_input == "exit" or user_input == "":
            break

        output = run_conversation(INITIAL_MESSAGES, user_input)
        print(output)