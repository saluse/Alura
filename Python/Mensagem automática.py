from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# abrir o Chrome
driver = webdriver.Chrome()

# carregar o WhatsApp Web
driver.get("https://web.whatsapp.com/")

# aguardar o usuário fazer login no WhatsApp Web
input("Faça login no WhatsApp Web e pressione Enter")

# encontrar o campo de pesquisa
search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')

# digitar o nome ou número do contato
search_box.send_keys("Vida")
search_box.send_keys(Keys.ENTER)

# encontrar a caixa de mensagem
message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

# digitar a mensagem
message_box.send_keys("Mensagem enviada pelo Python")

# enviar a mensagem
send_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
send_button.click()

# aguardar alguns segundos para a mensagem ser enviada
time.sleep(5)

# fechar o navegador
driver.quit()
