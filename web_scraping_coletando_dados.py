from    bs4         import BeautifulSoup    # pip install beautifulsoup4
import  requests                            # pip install requests


# URL do site consultado | Salva codigo HTML na variável html | Salva visualização personalizada na variável soup
# ****************************************************************************************************************

url = "https://www.climatempo.com.br/previsao-do-tempo/cidade/271/curitiba-pr"
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')  # https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/

# print(soup)


# Atribuindo valores as variáveis conforme ID do HTML
# Passando o tipo de elemento como | span | div | a busca fica mais rapida
# ****************************************************************************************************************

temp_min  = soup.find("span", id="min-temp-1")
temp_max  = soup.find("span", id="max-temp-1")


# Atribuindo valores as variáveis conforme ID do HTML
# ****************************************************************************************************************

if temp_max and temp_min:
  
  print(f"\n{soup.title.string}")
  print(f"\nTemperatura MINIMA hoje em Curitiba: {temp_min.string}")
  print(f"\nTemperatura MAXIMA hoje em Curitiba: {temp_max.string}")

  # print(f"\n\n{soup.find_all('img')}") # Buscando por TAGS específicas

else:
  print("Verificar ID na pagina HTML.")


# "https://solucoes.receita.fazenda.gov.br/Servicos/certidaointernet/PJ/Consultar/"
