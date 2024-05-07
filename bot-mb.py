import os, random
import discord, requests
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')


@bot.command('manualidades')
async def img(ctx):
    descriptions = {
        "manure1.jpg": "con una lata de metal, tapas y cuerda, haces un macetero colgante, perforas la lata en 4 y pasas la cuerda despues pegas las tapas y adentro de la lata pones tierra y una semilla y la vas regando.",
        "manure2.jpg": "con una botella de plastico y un trapo, haces un macetero que se riega solo, cortas la botella por la mitad en la parte superior pasas el trapo y en la parte de abajo pones agua ahora los juntas cono en la foto y pones tierra y una semilla ('solo tienes que preocuparte porque no se ponga verde el agua o que ya no tenga agua')",
        "manure3.jpg": "con un neumatico y una tabla de madera, haces un macetero grande, cortas la tabla de madera con el diametro de el neumatico y le pones tierra, agua, tierra y la semilla ",
        "manure4.jpg": "con una botella de plastico y cuerda, haces un bolso miniatura, cortas la botella en la mitad haces 4 hoyos en cada mitad y pasas la cuerda y le haces un nudo ",
        "manure5.jpg": "con 2 botellas de plastico, carton y arena, haces un reloj de arena, cortas la parte superior de ambas botellas y las pegas y cortas 2 trosos de carton con el diametro de cada hoyo de las partes superiores y pegas un troso de carton hechas hasta la mitad de arena y con el otro troso de carton lo cerras",
        "manure6.jpg": "con 2 palet (caja de madera), puedes hacer una cama, una silla y una silla inclinada, unes los 2 palet pero dejas que se puedan separar y dejas un hoyo en un poco menos del medio y con unas tablas o recortes de los palets haces un cajoncito y lo pones en la parte de abajo y que pueda moverse hacia adelante y esconder",
        "manure7.jpg": "papel, lana, colores y pelota amarilla, haces una decoracion de abejas, haces un circulo de 6 lados con el papel lo recortas en 19 o mas trosos y la pintas amarillo y lo pegas, envuelves las pelotas amarillas con la lana y le haces una cara y juntas el panel de papel con las abejitas y lo pegas en la pared",
        "manure8.jpg": "con unos perros de ropa y un plumon, haces un cocodrilo de decoracion, pegas el perro de ropa a la pared y dibujas un cocodrilo con el cuerpo de un perro de ropa"
    }
    img_name = random.choice(os.listdir("imagenes"))
    with open(f'imagenes/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    if img_name in descriptions:
        await ctx.send(descriptions[img_name])
    else:
        await ctx.send("No se encontró una descripción para esta imagen.")


@bot.command('contaminacion')
async def wiki(ctx):
    await ctx.send("Aquí tienes el enlace a la página de Wikipedia sobre contaminación: https://es.wikipedia.org/wiki/Contaminaci%C3%B3n")
bot.run("TOKEN")
