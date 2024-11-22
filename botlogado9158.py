import requests
import discord
from discord.ext import tasks, commands
import time
from tokens import token
url = "https://api.battlemetrics.com/servers/27038370"

ID_CANAL = 1265507071873257572

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)

ultima_contagem_jogadores = None
variacao_jogadores = 0
contagem_inicial_jogadores = None
tempo_ultimo_reset = None
ultima_mensagem = None
qtd = 0
danger = 0

async def obter_info_servidor():
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        nome_servidor = dados['data']['attributes']['name']
        try:
            contagem_jogadores = int(dados['data']['attributes']['players'])
        except ValueError:
            contagem_jogadores = None
        return nome_servidor, contagem_jogadores
    except requests.RequestException as e:
        print(f"Erro na requisição à API: {e}")
        return None, None

@bot.event
async def on_ready():
    global ultima_contagem_jogadores, variacao_jogadores, contagem_inicial_jogadores, tempo_ultimo_reset, nome_servidor
    print(f'Logado como {bot.user}')
    
    nome_servidor, contagem_inicial_jogadores = await obter_info_servidor()
    if contagem_inicial_jogadores is None:
        print("Erro ao obter a contagem inicial de jogadores.")
        return
    
    ultima_contagem_jogadores = contagem_inicial_jogadores
    variacao_jogadores = 3
    tempo_ultimo_reset = bot.loop.time()
    
    if not monitorar_servidor.is_running():
        monitorar_servidor.start()

@tasks.loop(minutes=1)
async def monitorar_servidor():
    global ultima_contagem_jogadores, variacao_jogadores, contagem_inicial_jogadores, tempo_ultimo_reset, ultima_mensagem, qtd, danger
    
    canal = bot.get_channel(ID_CANAL)
    nome_servidor, contagem_jogadores = await obter_info_servidor()
    tempo_atual = bot.loop.time()
    
    if nome_servidor and contagem_jogadores is not None:
        variacao = contagem_jogadores - ultima_contagem_jogadores
        variacao_jogadores += variacao
        ultima_contagem_jogadores = contagem_jogadores

        mencao = ""
        if 3 <= variacao_jogadores < 5:
            mencao = "@here " * 3
            danger = 1
        elif variacao_jogadores >= 5:
            mencao = "@everyone"
            qtd += 1
            if qtd >= 5:
                variacao_jogadores = 0
                danger = 0
        if danger == 0:
            simbolo = "+"
        else:
            simbolo = "-"

        mensagem = (
            "```Diff\n" + simbolo + f" Servidor: {nome_servidor}\n"
            "" + simbolo + f" Quantidade de jogadores: {contagem_jogadores}\n"
            "" + simbolo + f" Variação de jogadores nos últimos 20 min: {variacao_jogadores}\n```"
        )
        if mencao:
            mensagem = f"{mencao}\n{mensagem}"

        try:
            await ultima_mensagem.delete()
        except Exception as e:
            print(f"Erro ao deletar a mensagem anterior: {e}")

        ultima_mensagem = await canal.send(mensagem)

        if tempo_atual - tempo_ultimo_reset >= 1200:  # 20 minutos em segundos
            variacao_jogadores = contagem_jogadores - contagem_inicial_jogadores
            tempo_ultimo_reset = tempo_atual
            contagem_inicial_jogadores = contagem_jogadores
            danger = 0
    else:
        print("Erro ao pegar dados do servidor")

@bot.command(name="reset")
async def reset_variacao(ctx):
    global variacao_jogadores, danger
    if ctx.channel.id == ID_CANAL:
        variacao_jogadores = 0
        danger = 0
        await ctx.send(":thumbsup:")

try:
    bot.run(token)
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    time.sleep(5)
    bot.run(token)
