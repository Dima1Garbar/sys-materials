import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text

def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    tdd = soup.find('span', class_="x-hidden")
    return float(tdd.span.text.strip())

def main(a, b, c, d):
    # c - вибір частини кімнати
    # b - вибір вид
    # a - ціна основного матеріала
    # d - ціна 2 матеріала
    my_parse = None
    if c == 3:

        if b == 1:

            if a == 1:
                my_parse = parse(get_html('https://prom.ua/ua/p797847120-plita-armstrong-oasis.html'))
            elif a == 2:
                my_parse = parse(get_html('https://prom.ua/ua/p885691643-plita-armstrong-sierra.html'))
            elif a == 3:
                my_parse = parse(get_html('https://prom.ua/ua/p939160414-plita-armstrong-sierra.html'))
            elif d == 1:
                my_parse = parse(get_html('https://prom.ua/ua/p320537570-klej-dlya-penoplasta.html'))
            elif d == 2:
                my_parse = parse(get_html('https://prom.ua/ua/p320537775-klej-dlya-penoplasta.html'))
            elif d == 3:
                my_parse = parse(get_html('https://prom.ua/ua/p374358058-kreisel-klej-dlya.html'))

        if b == 2:

            my_parse = parse(get_html('https://prom.ua/ua/p5384226-potolki-natyazhnye-matovye.html'))

    if c == 2:

        if b == 1:

            if a == 1:
                my_parse = parse(get_html('https://prom.ua/ua/p191811381-linoleum-tkanevoj-osnove.html'))
            elif a == 2:
                my_parse = parse(get_html('https://prom.ua/ua/p890324076-gomogennyj-kommercheskij-linoleum.html'))
            elif a == 3:
                my_parse = parse(get_html('https://prom.ua/ua/p544760246-forbo-cocoa-358135.html'))

        if b == 2:

            if a == 1:
                my_parse = parse(get_html('https://prom.ua/ua/p244422843-parketnaya-doska-diana.html'))
            elif a == 2:
                my_parse = parse(get_html('https://prom.ua/ua/p959155011-parket-polarwood-dub.html'))
            elif a == 3:
                my_parse = parse(get_html('https://prom.ua/ua/p958427314-parket-polarwood-dub.html'))

        if b == 3:

            if a == 1:
                my_parse = parse(get_html('https://prom.ua/ua/p863835341-plitka-centurial-napolnaya.html'))
            elif a == 2:
                my_parse = parse(get_html('https://prom.ua/ua/p816249953-solfatara-bezh-tyomnyj.html'))
            elif a == 3:
                my_parse = parse(get_html('https://prom.ua/ua/p586061878-plitka-abk-sensi.html'))
            if d == 1:
                my_parse = parse(get_html('https://prom.ua/ua/p860741273-anserglob-bcx-40klej.html'))
            elif d == 2:
                my_parse = parse(get_html('https://prom.ua/ua/p804951557-baumit-flextop-elastichnaya.html'))
            elif d == 3:
                my_parse = parse(get_html('https://prom.ua/ua/p937553590-mapei-keraflex-extra.html'))

    if c == 1:

        if b == 1:

            if a == 1:
                my_parse = parse(get_html('https://prom.ua/ua/p849744176-oboi-dupleksnye-slavyanskie.html'))
            elif a == 2:
                my_parse = parse(get_html('https://prom.ua/ua/p770071667-oboi-shpaleri-rasch.html'))
            elif a == 3:
                my_parse = parse(get_html('https://prom.ua/ua/p707298172-oboi-creation-pro.html'))

        elif b == 2:

            if a == 1:
                my_parse = parse(get_html('https://prom.ua/ua/p724116429-shlifovka-parketa.html'))
            elif a == 2:
                my_parse = parse(get_html('https://prom.ua/ua/p562838762-doska-pola-110.html'))
            elif a == 3:
                my_parse = parse(get_html('https://prom.ua/ua/p123947217-doska-pola-shpuntirovannaya.html'))

        elif b == 3:
            if a == 1:
                my_parse = parse(get_html('https://prom.ua/ua/p863835341-plitka-centurial-napolnaya.html'))
            elif a == 2:
                my_parse = parse(get_html('https://prom.ua/ua/p816249953-solfatara-bezh-tyomnyj.html'))
            elif a == 3:
                my_parse = parse(get_html('https://prom.ua/ua/p586061878-plitka-abk-sensi.html'))
            if d == 1:
                my_parse = parse(get_html('https://prom.ua/ua/p860741273-anserglob-bcx-40klej.html'))
            elif d == 2:
                my_parse = parse(get_html('https://prom.ua/ua/p804951557-baumit-flextop-elastichnaya.html'))
            elif d == 3:
                my_parse = parse(get_html('https://prom.ua/ua/p937553590-mapei-keraflex-extra.html'))
    return my_parse

