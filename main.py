import requests
import time
import json
from datetime import datetime

class TelegramBot:
  def __init__(self):
    token = '1494075568:AAE6Wsi24XI762ntKvLTH2m30M4vnLYv8k4'
    self.url_base = 'https://api.telegram.org/bot' + token

  def Initiate(self):
    update_id = None
    while True:
      update = self.get_messages(update_id)
      
      #DEBUG
      # data_e_hora_atuais = datetime.now()
      # data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
      # print(update)
      # print(data_e_hora_em_texto)

      messages = update['result']
      if messages:
        for message in messages: 
          update_id = message['update_id']
          chat_id = message['message']['from']['id']
          first_interaction = message['message']['message_id'] == 1
          
          print(message['message']['message_id'])

          answer = self.create_answer(message, first_interaction)
          self.responder(answer, chat_id)

  def get_messages(self, update_id):
    link_requisicao = self.url_base + '/getUPdates?timeout=100'
    if update_id:
      link_requisicao = link_requisicao + '&offset=' + str((update_id + 1))
    resultado = requests.get(link_requisicao)
    return json.loads(resultado.content)

  def create_answer(self, message, first_interaction):
    if(first_interaction):
      return "eu nao funciono direito"
    else:
      return 'oi'

  def responder(self, resposta, chat_id):
    link_envio = self.url_base + '/sendMessage?chat_id=' + str(chat_id) + '&text=' + resposta
    requests.get(link_envio)



bot = TelegramBot()
bot.Initiate()



  #TODO loop semanal para crawlear o site de patch notes

