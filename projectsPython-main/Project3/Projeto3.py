# Importando bases | de dados do Excel | Importando bibliotecas | Webdriver Usando Selenium #

from selenium import webdriver
import pandas as pd
import unicodedata

navegador = webdriver.Chrome()
navegador.get("https://www.google.com/")

tabela = pd.read_excel("Project3/commodities.xlsx")
print(tabela)


for linha in tabela.index:
    produto = tabela.loc[linha, "Produto"]
    
    print(produto)
    produto = produto.replace("ó", "o").replace("ã", "a").replace("á", "a").replace(
    "ç", "c").replace("ú", "u").replace("é", "e")
    
    link = f"https://www.melhorcambio.com/{produto}-hoje"
    print(link)
    navegador.get(link)

    preco = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
    preco = preco.replace(".", "").replace(",", ".")
    print(preco)
    tabela.loc[linha, "Preço Atual"] = float(preco)


print("Acabou")
print(tabela)