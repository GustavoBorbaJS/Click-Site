import pyautogui
import time

# Aguarde alguns segundos para preparar o ambiente
time.sleep(3)

# Abrir o navegador (no exemplo, usamos o Chrome)
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# Aguarde o navegador ser aberto
time.sleep(5)

# Digitar a pesquisa no Google
pesquisa = "Exemplo de automação de tarefas com Python"
pyautogui.write(pesquisa)
pyautogui.press('enter')

# Aguarde os resultados da pesquisa carregarem
time.sleep(5)

# Clicar no primeiro resultado
pyautogui.click(x=400, y=300)

# Aguarde alguns segundos para ver o resultado
time.sleep(5)

# Fechar o navegador
pyautogui.hotkey('ctrl', 'w')
