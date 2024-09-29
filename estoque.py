import pandas as pd
import tkinter as tk
from tkinter import messagebox, filedialog

# Função para criar um DataFrame inicial vazio
def criar_dataframe_vazio():
    return pd.DataFrame(columns=['Item', 'Quantidade', 'Estoque Mínimo'])

# Definindo os valores mínimos
estoque_minimo = {
    'Balão': 50,
    'Paraquedas': 50,
    'Sonda': 40
}

# 1. Função para carregar os dados de um arquivo CSV
def carregar_estoque():
    arquivo = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    if arquivo:
        global estoque_df
        estoque_df = pd.read_csv(arquivo)
        atualizar_labels()
        messagebox.showinfo("Carregar", "Estoque carregado com sucesso!")
    else:
        estoque_df = criar_dataframe_vazio()  # Se não carregar, cria um DataFrame vazio

# 2. Função para verificar estoque baixo
def verificar_estoque_baixo(df):
    return df[df['Quantidade'] < df['Estoque Mínimo']]

# 3. Função para atualizar a quantidade de itens em estoque
def atualizar_estoque(item, quantidade):
    if item in estoque_df['Item'].values:
        estoque_df.loc[estoque_df['Item'] == item, 'Quantidade'] += quantidade
        messagebox.showinfo("Atualização", f"{quantidade} unidades de {item} foram atualizadas.")
        verificar_e_exibir_estoque_baixo()
        atualizar_labels()  # Atualiza os rótulos após a atualização
    else:
        messagebox.showerror("Erro", f"O item '{item}' não foi encontrado no estoque.")

# 4. Função para verificar e exibir aviso de estoque baixo
def verificar_e_exibir_estoque_baixo():
    itens_baixos = verificar_estoque_baixo(estoque_df)
    if not itens_baixos.empty:
        aviso = "Aviso: Os seguintes itens estão com estoque baixo:\n"
        aviso += itens_baixos.to_string(index=False)
        messagebox.showwarning("Estoque Baixo", aviso)

# 5. Função para listar itens em estoque
def listar_itens():
    lista = estoque_df.to_string(index=False)
    messagebox.showinfo("Itens em Estoque", lista)

# 6. Função para atualizar os rótulos com as quantidades atuais
def atualizar_labels():
    for item in estoque_df['Item']:
        if item == 'Balão':
            label_quantidade_balao.config(
                text=f"Quantidade Atual: {estoque_df.loc[estoque_df['Item'] == 'Balão', 'Quantidade'].values[0]}")
            estoque_df.loc[estoque_df['Item'] == 'Balão', 'Estoque Mínimo'] = estoque_minimo['Balão']
        elif item == 'Paraquedas':
            label_quantidade_paraquedas.config(
                text=f"Quantidade Atual: {estoque_df.loc[estoque_df['Item'] == 'Paraquedas', 'Quantidade'].values[0]}")
            estoque_df.loc[estoque_df['Item'] == 'Paraquedas', 'Estoque Mínimo'] = estoque_minimo['Paraquedas']
        elif item == 'Sonda':
            label_quantidade_sonda.config(
                text=f"Quantidade Atual: {estoque_df.loc[estoque_df['Item'] == 'Sonda', 'Quantidade'].values[0]}")
            estoque_df.loc[estoque_df['Item'] == 'Sonda', 'Estoque Mínimo'] = estoque_minimo['Sonda']

# 7. Função para manipular o botão de atualização
def atualizar_todos():
    try:
        quantidade_balao = int(entry_balao.get())
        quantidade_paraquedas = int(entry_paraquedas.get())
        quantidade_sonda = int(entry_sonda.get())

        atualizar_estoque('Balão', quantidade_balao)
        atualizar_estoque('Paraquedas', quantidade_paraquedas)
        atualizar_estoque('Sonda', quantidade_sonda)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira quantidades válidas.")

# 8. Função para salvar os dados em um arquivo CSV
def salvar_estoque():
    arquivo = filedialog.asksaveasfilename(defaultextension=".csv",
                                             filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    if arquivo:
        estoque_df.to_csv(arquivo, index=False)
        messagebox.showinfo("Salvar", "Estoque salvo com sucesso!")

# 9. Criação da interface gráfica
app = tk.Tk()
app.title("Gerenciamento de Estoque")

# Inicializa o DataFrame
estoque_df = criar_dataframe_vazio()

# Frame para entrada de dados
frame_entrada = tk.Frame(app)
frame_entrada.pack(pady=10)

# Labels e Entradas para cada item
label_balao = tk.Label(frame_entrada, text="Balão:")
label_balao.grid(row=0, column=0, padx=5)
entry_balao = tk.Entry(frame_entrada)
entry_balao.grid(row=0, column=1, padx=5)
label_quantidade_balao = tk.Label(frame_entrada, text="Quantidade Atual: 0")
label_quantidade_balao.grid(row=0, column=2, padx=5)

label_paraquedas = tk.Label(frame_entrada, text="Paraquedas:")
label_paraquedas.grid(row=1, column=0, padx=5)
entry_paraquedas = tk.Entry(frame_entrada)
entry_paraquedas.grid(row=1, column=1, padx=5)
label_quantidade_paraquedas = tk.Label(frame_entrada, text="Quantidade Atual: 0")
label_quantidade_paraquedas.grid(row=1, column=2, padx=5)

label_sonda = tk.Label(frame_entrada, text="Sonda:")
label_sonda.grid(row=2, column=0, padx=5)
entry_sonda = tk.Entry(frame_entrada)
entry_sonda.grid(row=2, column=1, padx=5)
label_quantidade_sonda = tk.Label(frame_entrada, text="Quantidade Atual: 0")
label_quantidade_sonda.grid(row=2, column=2, padx=5)

# Botão para atualizar todos os itens
botao_atualizar_todos = tk.Button(app, text="Atualizar Estoque de Todos os Itens", command=atualizar_todos)
botao_atualizar_todos.pack(pady=5)

# Botão para listar itens
botao_listar = tk.Button(app, text="Listar Itens em Estoque", command=listar_itens)
botao_listar.pack(pady=5)

# Botões para salvar e carregar
botao_salvar = tk.Button(app, text="Salvar Estoque", command=salvar_estoque)
botao_salvar.pack(pady=5)

# Tenta carregar o estoque ao iniciar
carregar_estoque()

# Atualiza os rótulos após carregar o estoque
atualizar_labels()

# Iniciar a interface
app.mainloop()
