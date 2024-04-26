# # https://www.selenium.dev/pt-br/documentation/webdriver/browsers/chrome/
# ****************************************************************************************************


from    bs4                                 import BeautifulSoup        # pip install beautifulsoup4
import  requests                                                        # pip install requests
                                                                        # pip install selenium
from    selenium                            import webdriver            # pip install webdriver-manager
from    webdriver_manager.chrome            import ChromeDriverManager
from    selenium.webdriver.chrome.service   import Service
import  time
import  os

servico     = Service(ChromeDriverManager().install())
navegador   = webdriver.Chrome(service=servico)


navegador.get("https://solucoes.receita.fazenda.gov.br/Servicos/certidaointernet/PJ/Consultar/")
time.sleep(2)

navegador.find_element('xpath',
                       '//*[@id="Ni"]'
                      ).send_keys("08.723.151/0001-80")
time.sleep(5)


navegador.find_element('xpath',
                       '//*[@id="PeriodoInicio"]'
                      ).send_keys("25042024")
time.sleep(2)

navegador.find_element('xpath',
                       '//*[@id="PeriodoFim"]'
                      ).send_keys("25042024")
time.sleep(5)

navegador.find_element('xpath',
                       '//*[@id="validar"]'
                      ).click()

time.sleep(20)



