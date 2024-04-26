# # https://www.selenium.dev/pt-br/documentation/webdriver/browsers/chrome/
# ****************************************************************************************************


from    bs4                                 import BeautifulSoup        # pip install beautifulsoup4
import  requests                                                        # pip install requests
                                                                        # pip install selenium
from    selenium                            import webdriver            # pip install webdriver-manager
from    webdriver_manager.chrome            import ChromeDriverManager
from    selenium.webdriver.chrome.service   import Service
import  time

servico     = Service(ChromeDriverManager().install())
navegador   = webdriver.Chrome(service=servico)


navegador.get("https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M")
time.sleep(2)

navegador.find_element('xpath',
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input'
                      ).send_keys("Thiago")
time.sleep(2)

navegador.find_element('xpath',
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input'
                      ).send_keys("thiago@gmail.com")
time.sleep(2)

navegador.find_element('xpath',
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[3]/div/input'
                      ).send_keys("41999117200")
time.sleep(2)

navegador.find_element('xpath',
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/button/span/b'
                      ).click()
time.sleep(10)
