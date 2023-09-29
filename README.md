# previsao_tempo_rpc

<img width="179" alt="image" src="https://github.com/vinisann/previsao_tempo_rpc/assets/79290745/0e17530b-bcf1-476b-8eb9-6a7d8076c836">
<img width="178" alt="image" src="https://github.com/vinisann/previsao_tempo_rpc/assets/79290745/3cecfcd6-6c34-4e59-82af-3922aa596125">



Este código foi feito para estudo de API e servidor RPC, que fornece um método para retornar a previsão do tempo para uma cidade específica. O servidor utiliza a API da OpenWeatherMap para obter os dados da previsão do tempo.

# Como usar
Para usar o servidor, siga estas etapas:

# Instale as bibliotecas necessárias:
pip install rpyc
pip install requests
Execute o servidor:
python servidor.py
Funcionamento

# O servidor funciona da seguinte forma:
O servidor recebe uma solicitação do cliente.
O servidor obtém os dados da previsão do tempo da API da OpenWeatherMap.
O servidor retorna os dados da previsão do tempo para o cliente.

# Requisitos
Python 3.6 ou superior
Biblioteca RPC do Python
Biblioteca Requests
Cliente

# O cliente funciona da seguinte forma:
Instale as bibliotecas necessárias:
pip install rpyc
pip install tkinter
Execute o cliente:
python cliente.py
Digite o nome da cidade na qual deseja consultar a previsão do tempo.
Clique no botão "Consultar".

# Funcionamento
O cliente funciona da seguinte forma:
O cliente se conecta ao servidor RPC na porta 18812.
O cliente chama o método exposed_previsao_do_tempo() do servidor RPC.
O servidor retorna os dados da previsão do tempo para o cliente.
O cliente formata os dados da previsão do tempo e os exibe em uma janela.

# Requisitos
Python 3.6 ou superior
Biblioteca RPC do Python
Biblioteca Tkinter
Contribuições

Contribuições são bem-vindas :)
