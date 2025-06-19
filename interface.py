
from model_loader import load_model
from chat_memory import ChatMemory

def main():
    chatbot = load_model()
    memory = ChatMemory(max_turns=5)

    print("Chatbot started. Type /exit to quit.")
    while True:
        user_input = input("User: ")
        if user_input.strip().lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break
      
        context = memory.get_context() + f"\nUser: {user_input}\nBot:"
        response = chatbot(context, max_new_tokens=100, do_sample=True)[0]["generated_text"]

       
        bot_reply = response.split("Bot:")[-1].strip()
        bot_reply = bot_reply.split(".")[0].strip() + "."  

        print(f"Bot: {bot_reply}")
        memory.add_turn(user_input, bot_reply)



if __name__ == "__main__":
    main()
