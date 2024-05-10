#Passo a passo

# instalar biblioteca: pip install pyautogui

import pyautogui as pygui #importa a biblioteca / "as pygui" é uma abreviação de pyautogui
import time
import pandas as pd

pygui.PAUSE = 0.5

# pygui.click -> clicar com o mouse
# pygui.write -> escrever
# pygui.press -> pressionar tecla
# pygui.hotkey -> pressionar um conjunto de teclas(ctrl c, ctrl v, Alt tab)

#1. Abrir o navegador

pygui.press("win")
pygui.write("brave")
pygui.press("enter")

#2. Abrir sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

pygui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pygui.press("enter")

#aqui pode ser que demora alguns segundos para carregar o site
time.sleep(2)

#2.1 Fazer login
    #guilherme.langher@gmail.com
    #senha: 123456

#Utilizando o "pyautogui.click" para utilizar o mouse

pygui.click(x=700, y=452)
pygui.write("guilherme.langher@gmail.com")
pygui.press("tab")
pygui.write("123456")
pygui.press("enter")

#Utilizando apenas o teclado

#pygui.press("tab")
#pygui.write("guilherme.langher@gmail.com")
#pygui.press("tab")
#pygui.write("123456")
#pygui.press("enter")

time.sleep(2)

#3. Abrir a base de dados de produto
#pip install pandas numpy openpyxl
#importar essas bibliotecas

tabela = pd.read_csv("produtos.csv")

#4.0 Cadastrar o primeiro produto

for linha in tabela.index:

    codigo = str(tabela.loc[linha, "codigo"])
    marca = str(tabela.loc[linha, "marca"])
    tipo = str(tabela.loc[linha, "tipo"])
    categoria = str(tabela.loc[linha, "categoria"])
    preco = str(tabela.loc[linha, "preco_unitario"])
    custo = str(tabela.loc[linha, "custo"])
    obs = str(tabela.loc[linha, "obs"])

    #4.1 Clicar no campo do codigo do produto
    pygui.click(x=713, y=317)

    #4.2 Preencher o codigo do produto
    pygui.write(codigo)

    #4.3 Passar para o proximo campo 
    pygui.press("tab")

    #marca
    pygui.write(marca)
    pygui.press("tab")

    #tipo
    pygui.write(tipo)
    pygui.press("tab")

    #categoria
    pygui.write(categoria)
    pygui.press("tab")

    #preco
    pygui.write(preco)
    pygui.press("tab")

    #custo
    pygui.write(custo)
    pygui.press("tab")

    #obs
    if obs != "nan": #se a variavel for diferente de "nan" o codigo vai seguir e preencher o campo obs
        pygui.write(obs)
        6.5     
        pygui.press("tab")

    #enviar produto cadastrado
    pygui.press("enter")
    pygui.scroll(5000)


#5. Repetir até acabar a lista de produtos 


