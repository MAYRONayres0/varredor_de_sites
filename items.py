# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Join
import json



def limpar_texto(texto):
    return texto.strip()

def tirar_caracter_especial(valor):
   return valor.replace("\n",'').replace("“",'')

def mudar_virgula(valor):
    return valor.replace(",",';')

def replace_ampersand(value):
    return value.replace("&amp;", "-")

def letra_maiuscula(valor):
    return valor.upper()


class citacao_frases(scrapy.Item):
   frase = scrapy.Field(
       input_processor=MapCompose(limpar_texto,tirar_caracter_especial),
       output_processor =TakeFirst()
   )
   
   autor = scrapy.Field(
       input_processor=MapCompose(limpar_texto,tirar_caracter_especial,letra_maiuscula),
       output_processor = TakeFirst()
   )
   
   tags = scrapy.Field(
       input_processor = MapCompose(mudar_virgula,letra_maiuscula),
       output_processor=Join(',')
   )

#                                           TEATRO
class citacap_frases1(scrapy.Item):
    show =  scrapy.Field(
    input_processor= MapCompose(replace_ampersand),
    output_processor=TakeFirst()
) 
    local = scrapy.Field(
    input_processor = MapCompose(letra_maiuscula),
    output_processor= TakeFirst()
)
    data = scrapy.Field(
    output_processor=TakeFirst()
)