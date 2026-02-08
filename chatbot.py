from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


bot= ChatBot("chatbot :", read_only=False ,logic_adapters=[
    {
        "import_path": "chatterbot.logic.BestMatch",
        "default_response":"Sorry! I don't have any answer for this",
        "maximum_similarity_threshold":0.9
        }
        ])
list_to_train=[
                "hello",
                "Hi!!",
                "How are you?",
                "I'm fine, thanks!",
                "bye",
                "Goodbye!"
]
list_trainer=ListTrainer(bot)

list_trainer.train(list_to_train)


print("Chatbot : Hello! Type 'bye' to exit" )

while True:
    user_response = input("User: ")
    print("Chatbot: ",bot.get_response(user_response))

    if user_response=="bye":
        break