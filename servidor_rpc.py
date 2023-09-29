import rpyc #Importa a biblioteca de RPC (Remote Procedure Call)
from rpyc.utils.server import ThreadedServer # classe para criar um servidor RPC
import requests

API_KEY = "Digite aqui sua API gerada do site OpenWeatherMap"

class MyService(rpyc.Service):
    
    #Método para retornar a previsão do tempo para uma cidade específica
    def exposed_previsao_do_tempo(self, cidade):
        
        #URL da API da OpenWeatherMap.
        link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"
        #Faz uma requisição GET da API e armazena a resposta em um dicionário em arquivo JSON.
        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()
        #Extrai os dados da previsão do tempo do dicionário.
        descricao = requisicao_dic['weather'][0]['description']
        temperatura_atual = requisicao_dic['main']['temp'] - 273.15
        temperatura_minima = requisicao_dic['main']['temp_min'] - 273.15
        temperatura_maxima = requisicao_dic['main']['temp_max'] - 273.15
        sensacao_termica = requisicao_dic['main']['feels_like'] - 273.15
        umidade_ar = requisicao_dic['main']['humidity']
        #Retorna os dados da previsão do tempo
        return(descricao, temperatura_atual, temperatura_minima, temperatura_maxima, sensacao_termica, umidade_ar)
    
if __name__ == "__main__":
    # configura e inicia o servidor na rede local
    server = ThreadedServer(MyService, hostname='0.0.0.0', port=18812)
    print('Servidor online')
    server.start()
