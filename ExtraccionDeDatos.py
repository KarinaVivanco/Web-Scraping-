import requests
from lxml import html
encabezados = {
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
url = "https://www.wikipedia.org/"

respuesta = requests.get(url, headers=encabezados)

parser = html.fromstring(respuesta.text)

ingles = parser.get_element_by_id("js-link-box-en")
print(ingles.text_content())

idiomas = parser.find_class('central-featured-lang')
for idioma in idiomas:
    print(idioma.text_content())