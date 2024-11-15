import requests
import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def cidade():
    cidade = entrada.get()

    api_key = ""
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={cidade}&lang=pt"

    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()

        temperatura_c = dados["current"]["temp_c"]
        temperatura_f = dados["current"]["temp_f"]
        sensacao_termica_c = dados["current"]["feelslike_c"]
        sensacao_termica_f = dados["current"]["feelslike_f"]
        uv = dados["current"]["uv"]
        velocidade_vento_mph = dados["current"]["wind_mph"]
        umidade = dados["current"]["humidity"]
        descricao = dados["current"]["condition"]["text"]

        resultado_label.configure(text=(
            f"O clima em {cidade} é de {temperatura_c}°C ({temperatura_f}°F) com {descricao}.\n"
            f"Sensação térmica: {sensacao_termica_c}°C ({sensacao_termica_f}°F)\n"
            f"Incidência de ultravioleta (UV): {uv}\n"
            f"Velocidade do vento: {velocidade_vento_mph} mph\n"
            f"Umidade: {umidade}%"
        ))
    else:
        resultado_label.configure(text="Erro ao obter dados da API.")

root_tk = tk.Tk()
root_tk.geometry("400x600")
root_tk.title("Previsão do Tempo")

root_tk.configure(bg="#1c1c1c")

titulo_label = ctk.CTkLabel(
    root_tk, 
    text="Previsão do Tempo", 
    font=("Arial", 20, "bold"), 
    text_color="white"
)
titulo_label.pack(pady=20)

entrada = ctk.CTkEntry(
    root_tk, 
    placeholder_text="Digite o nome da cidade", 
    width=300, 
    font=("Arial", 14),
    fg_color="#2b2b2b",
    text_color="white"  
)
entrada.pack(pady=10, padx=20)

resultado = ctk.CTkButton(
    root_tk, 
    text="Pesquisar cidade", 
    command=cidade, 
    width=200, 
    height=40, 
    font=("Arial", 14, "bold"),
    fg_color="#3b3b3b",
    hover_color="#5a5a5a",
    text_color="white"
)
resultado.pack(pady=20)

resultado_label = ctk.CTkLabel(
    root_tk, 
    text="", 
    width=300, 
    height=200, 
    text_color="white",  
    font=("Arial", 14),
)
resultado_label.pack(pady=20, padx=20)

root_tk.mainloop()
