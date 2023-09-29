import rpyc #Importa a biblioteca de RPC (Remote Procedure Call)
import tkinter as tk #Importa a biblioteca tkinter de interface


def main():
    # Cria uma janela
    janela = tk.Tk()
    janela.title("Previsão do tempo")

    # Solicita a cidade ao usuário
    cidade = tk.Label(janela, text="Digite a sua cidade: ")
    cidade.grid(column=0, row=0, padx=10, pady=10)

    # Cria um campo de entrada para a cidade
    cidade_entrada = tk.Entry(janela)
    cidade_entrada.grid(column=1, row=0, padx=10, pady=10)

    # Cria um botão para consultar a previsão do tempo
    consultar = tk.Button(janela, text="Consultar", command=lambda: consultar_previsao(cidade_entrada.get(), janela.previsao_texto))
    consultar.grid(column=2, row=0, padx=10, pady=10)

    # Cria um rótulo para exibir a previsão do tempo
    janela.previsao_texto = tk.Label(janela, text="")
    janela.previsao_texto.grid(column=0, row=1, columnspan=3, padx=10, pady=10)
    janela.mainloop()


def consultar_previsao(cidade, previsao_texto):
    # Conecta-se ao servidor RPC na porta 18812
    with rpyc.connect("localhost", 18812) as conn:
        # Chama o método exposed_previsao_do_tempo()
        previsao = conn.root.exposed_previsao_do_tempo(cidade)

    # Formata os valores de temperatura com uma casa decimal
    previsao_formatada = (
        previsao[0],
        f"{previsao[1]:.0f}",
        f"{previsao[2]:.0f}",
        f"{previsao[3]:.0f}",
        f"{previsao[4]:.0f}",
        f"{previsao[5]:.0f}",
    )

    # Exibe a previsão do tempo
    previsao_texto.config(text=formatar_previsao(previsao_formatada))

#Formata a previsão do tempo e retorna o texto formatado, previsao_formatada: Uma lista com os valores da previsão do tempo formatados.
def formatar_previsao(previsao_formatada):
    

    # Retorna o texto formatado da previsão do tempo
    return f"Situação: {previsao_formatada[0].capitalize()}\n\n" \
           f"Temperatura atual: {previsao_formatada[1]} °C\n" \
           f"Temperatura mínima: {previsao_formatada[2]} °C\n" \
           f"Temperatura máxima: {previsao_formatada[3]} °C\n" \
           f"Sensação térmica: {previsao_formatada[4]} °C\n" \
           f"Umidade do ar: {previsao_formatada[5]}%"


if __name__ == "__main__":
    main()
