# %%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\Lucas\Downloads",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=options)

# %%
import os

caminho = os.getcwd()
arquivo = caminho + r'\login.html'
navegador.get(arquivo)

# %%
login =navegador.find_element(By.XPATH,'/html/body/div/form/input[1]').send_keys('lucas.amorim@email.com')
senha = navegador.find_element(By.XPATH, '/html/body/div/form/input[2]').send_keys(123456)
botao = navegador.find_element(By.XPATH,'/html/body/div/form/button').click()

# %%
import pandas as pd

df = pd.read_excel(r'C:\Users\Lucas\OneDrive\Curso\Hashtag\Python\automação web\Exercício - Automatizar Emissão de Nota Fiscal\NotasEmitir.xlsx')
df.head()


# %%
for linha in df.index:
    nome = navegador.find_element(By.ID, 'nome').send_keys(df.loc[linha, 'Cliente'])

    endereco = navegador.find_element(By.NAME, 'endereco').send_keys(df.loc[linha, 'Endereço'])

    bairro = navegador.find_element(By.NAME, 'bairro').send_keys(df.loc[linha, 'Bairro'])

    municipio = navegador.find_element(By.NAME, 'municipio').send_keys(df.loc[linha, 'Municipio'])

    cep = navegador.find_element(By.NAME, 'cep').send_keys(str(df.loc[linha,'CEP']))

    navegador.find_element(By.NAME, 'uf').send_keys(df.loc[linha,'UF'])

    cpf = navegador.find_element(By.NAME, 'cnpj').send_keys(str(df.loc[linha,'CPF/CNPJ']))

    incricao = navegador.find_element(By.NAME, 'inscricao').send_keys(str(df.loc[linha,'Inscricao Estadual']))

    descricao = navegador.find_element(By.NAME, 'descricao').send_keys(df.loc[linha,'Descrição'])

    quantidade = navegador.find_element(By.NAME, 'quantidade').send_keys(str(df.loc[linha,'Quantidade']))

    valor_unitario = navegador.find_element(By.NAME, 'valor_unitario').send_keys(str(df.loc[linha,'Valor Unitario']))

    total = navegador.find_element(By.NAME, 'total').send_keys(str(df.loc[linha,'Valor Total']))
    
    botao_clicar = navegador.find_element(By.CLASS_NAME,'registerbtn').click()

    navegador.refresh()

navegador.quit()

# %%



