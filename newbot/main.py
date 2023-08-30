import telebot
import requests 

import eth_transaction 
from verificar_hash import *
from eth_transaction import *
from eth_price import *

hash_comprador = ""
carteira_ethereum = "0x03fC32a7893487475617BeCF95A05813805b1D64"
CHAVE_API ="6572730398:AAFgC82qtUpExTnvkm_jWjbG6E2lYec_Pw8"

bot = telebot.TeleBot(CHAVE_API)

user_states = {}  # Dictionary to store user states

def verificar_transacao(mensagem, valor_plano):
    transacao_hash = mensagem.text
    status = eth_transaction.verificar_transacao_etherscan(transacao_hash, valor_plano, carteira_ethereum)
    bot.reply_to(mensagem, status)
    user_states.pop(mensagem.from_user.id, None)  # Remove user state after verification

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    user_states[mensagem.from_user.id] = "opcao1"  # Set user state to opcao1
    valor_plano = 15 / eth_price
    bot.send_message(mensagem.chat.id, "Please send:")
    bot.send_message(mensagem.chat.id, valor_plano)
    bot.send_message(mensagem.chat.id, "Eth To the following address")
    bot.send_message(mensagem.chat.id, carteira_ethereum)
    bot.send_message(mensagem.chat.id, "After sending the requested amount, please paste the hash transaction here.")

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    user_states[mensagem.from_user.id] = "opcao2"  # Set user state to opcao2
    valor_plano = 35 / eth_price
    bot.send_message(mensagem.chat.id, "Please send:")
    bot.send_message(mensagem.chat.id, valor_plano)
    bot.send_message(mensagem.chat.id, "Eth To the following address")
    bot.send_message(mensagem.chat.id, carteira_ethereum)
    bot.send_message(mensagem.chat.id, "After sending the requested amount, please paste the hash transaction here.")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    user_states[mensagem.from_user.id] = "opcao3"  # Set user state to opcao3
    valor_plano = 100 / eth_price
    bot.send_message(mensagem.chat.id, "Please send:")
    bot.send_message(mensagem.chat.id, valor_plano)
    bot.send_message(mensagem.chat.id, "Eth To the following address")
    bot.send_message(mensagem.chat.id, carteira_ethereum)
    bot.send_message(mensagem.chat.id, "After sending the requested amount, please paste the hash transaction here.")

@bot.message_handler(func=lambda mensagem: len(mensagem.text) == 66 and mensagem.from_user.id in user_states)
def verificar_transacao_handler(mensagem):
    if mensagem.chat.type == 'private':
        valor_plano = 15 / eth_price  # Default value
        if user_states[mensagem.from_user.id] == "opcao2":
            valor_plano = 35 / eth_price
        elif user_states[mensagem.from_user.id] == "opcao3":
            valor_plano = 100 / eth_price

        verificar_transacao(mensagem, valor_plano)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
     We only accept ETH
     Choose an option below (click on option)
    /opcao1 One Month $15.00
    /opcao2 Three Months $35.00
    /opcao3 Lifetime access $100.00"""

    bot.reply_to(mensagem, texto)



try:
    bot.polling()
except Exception as e:
    print("An error occurred while polling the bot:", e)
    # You can add more specific handling here if needed, like logging the error or sending a message to the developer.