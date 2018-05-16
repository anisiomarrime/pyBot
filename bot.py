from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot("MarrimeBot")
conversas = ["Olá, tudo bom ?", "Olá seja bem vindo, estou ótimo ! Em que posso lhe ser util :)",
"O que preciso para aprender a programar", "Simples amigo ! voce nao precisa ser um xtazzi da matematica"]
# Habilita o treino
bot.set_trainer(ListTrainer)
# Treina o bot um portugues
bot.train(conversas)

while True:
    msg = input("Voce: ")
    res = bot.get_response(msg)

    if float(res.confidence) > 0.5:
        print("MarrimeBot: ", res)
    else:
        print("MarrimeBot: Desculpa, Não entendi ?")