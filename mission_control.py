# ====================================================================
#  GLOBAL SOLUTION - PENSAMENTO COMPUTACIONAL E AUTOMAÇÃO COM PYTHON
# ====================================================================

# INTEGRANTES DO GRUPO:
# Kauanne Paula de Oliveira          RM:574191
# Nayhely Estela Calle Castillo      RM:571416

# ====================================================================
#             MISSION CONTROL AI: SISTEMA INTELIGENTE
#               DE MONITORAMENTO DE MISSÃO ESPACIAL
# ====================================================================

missao = "Guardian of Pegasus I"
equipe = "Equipe Space Knights"

# Criação dos ciclos de monitoramento

dados_missao = [
    [22, 95, 93, 98, 94],  # Ciclo 1 - Estável
    [25, 88, 85, 96, 88],  # Ciclo 2 - Pequena degradação
    [29, 75, 72, 93, 80],  # Ciclo 3 - Atenção inicial
    [33, 58, 55, 89, 68],  # Ciclo 4 - Atenção
    [37, 40, 35, 84, 52],  # Ciclo 5 - Próximo do crítico
    [39, 28, 18, 78, 38],  # Ciclo 6 - Crítico (pior momento)
    [35, 45, 30, 82, 50],  # Ciclo 7 - Recuperação inicial
    [31, 62, 48, 88, 65]   # Ciclo 8 - Recuperação consistente
]

# Áreas monitoradas da missão

areas_monitoradas = [
"Temperatura interna",
"Comunicação com a base",
"Sistema de energia",
"Suporte de oxigênio",
"Estabilidade operacional"
]

# Funções

def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1, "Baixa temperatura"
    elif 18 <= valor <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif 30 < valor <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"

def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2, "Comunicação com a base em nível crítico"
    elif 30 <= valor <= 59:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"

def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif 20 <= valor <= 49:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"

def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif 80 <= valor <= 89:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"

def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica"
    elif 40 <= valor < 69:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"

def classificar_ciclo(risco):
    if risco <= 2:
        return "MISSÃO ESTÁVEL"
    elif 3 <= risco <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"

def gerar_acoes(classificacoes):

    acoes = []

    # Temperatura
    if classificacoes[0] == "CRÍTICO":
        acoes.append(
            "Temperatura: Sistema de resfriamento emergencial ativado."
        )
    elif classificacoes[0] == "ATENÇÃO":
        acoes.append(
            "Temperatura: Ajuste preventivo do controle térmico realizado."
        )
    else:
        acoes.append(
            "Temperatura: Operação normal mantida."
        )

    # Comunicação
    if classificacoes[1] == "CRÍTICO":
        acoes.append(
            "Comunicação: Tentativa de restabelecimento do sinal executada."
        )
    elif classificacoes[1] == "ATENÇÃO":
        acoes.append(
            "Comunicação: Antenas recalibradas preventivamente."
        )
    else:
        acoes.append(
            "Comunicação: Comunicação estável."
        )

    # Bateria
    if classificacoes[2] == "CRÍTICO":
        acoes.append(
            "Bateria: Modo de economia de energia ativado."
        )
    elif classificacoes[2] == "ATENÇÃO":
        acoes.append(
            "Bateria: Consumo energético reduzido preventivamente."
        )
    else:
        acoes.append(
            "Bateria: Nível energético adequado."
        )

    # Oxigênio
    if classificacoes[3] == "CRÍTICO":
        acoes.append(
            "Oxigênio: Protocolo de suporte à vida acionado."
        )
    elif classificacoes[3] == "ATENÇÃO":
        acoes.append(
            "Oxigênio: Ajuste preventivo dos reservatórios realizado."
        )
    else:
        acoes.append(
            "Oxigênio: Níveis adequados."
        )

    # Estabilidade
    if classificacoes[4] == "CRÍTICO":
        acoes.append(
            "Estabilidade: Operações secundárias suspensas."
        )
    elif classificacoes[4] == "ATENÇÃO":
        acoes.append(
            "Estabilidade: Correções preventivas aplicadas."
        )
    else:
        acoes.append(
            "Estabilidade: Sistemas operando normalmente."
        )

    return acoes

def recomendacao_geral(risco_total):

    if risco_total <= 2:
        return "Missão estável. Manter monitoramento de rotina."

    elif risco_total <= 5:
        return "Missão em atenção. Intensificar monitoramento dos sistemas."

    else:
        return (
            "Missão crítica. Priorizar segurança, energia, "
            "comunicação e suporte à vida."
        )

def analisar_tendencia(riscos_ciclos_):

    maior_risco = max(riscos_ciclos_)
    ultimo_risco = riscos_ciclos[-1]

    if ultimo_risco < maior_risco:
        return "Recuperação após período crítico"

    elif ultimo_risco == maior_risco:
        return "Missão permanece em estado crítico"

    else:
        return "Risco crescente"

def calcular_media(dados_missao, coluna):
    soma = 0
    for ciclo in dados_missao:
        soma += ciclo[coluna]
    media = soma / len(dados_missao)
    return media

# Organização do cabeçalho do painel
print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)
print(f"Missão: {missao}")
print(f"Equipe: {equipe}")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
print("=" * 60)

# Criação de vetores para posterior avaliação da missão em si
riscos_ciclos = []
pontuacao_areas = [0, 0, 0, 0, 0]

# Organização e transformação de cada elemento dos ciclos em variaveis individuais
for indice, ciclo in enumerate(dados_missao, start=1):
    temperatura = ciclo[0]
    comunicacao = ciclo[1]
    bateria = ciclo[2]
    oxigenio = ciclo[3]
    estabilidade = ciclo[4]

    # Coletando os resultados de cada análise
    status_temp, risco_temp, descricao_temp = analisar_temperatura(temperatura)
    status_com, risco_com, descricao_com = analisar_comunicacao(comunicacao)
    status_bat, risco_bat, descricao_bat = analisar_bateria(bateria)
    status_oxi, risco_oxi, descricao_oxi = analisar_oxigenio(oxigenio)
    status_est, risco_est, descricao_est = analisar_estabilidade(estabilidade)

    # Aplicando os status de cada componente para posterior recomendações
    classificacoes = [
        status_temp,
        status_com,
        status_bat,
        status_oxi,
        status_est
    ]

    # Gerando as ações a serem tomadas de acordo com as classificações
    acoes = gerar_acoes(classificacoes)

    # Calculo do risco total de cada ciclo
    risco_total = (
        risco_temp +
        risco_com +
        risco_bat +
        risco_oxi +
        risco_est
    )

    # Registro do risco total de cada ciclo no vetor criado anteriormente
    riscos_ciclos.append(risco_total)

    # Registro da soma da pontuação de risco de cada área ao longo dos ciclos
    pontuacao_areas[0] += risco_temp
    pontuacao_areas[1] += risco_com
    pontuacao_areas[2] += risco_bat
    pontuacao_areas[3] += risco_oxi
    pontuacao_areas[4] += risco_est

    # Organização para exibição das informações obtidas de cada ciclo no painel
    print(f"\nCICLO {indice}")
    print("-" * 60)

    print(f"Temperatura: {temperatura}°C | {status_temp} | {descricao_temp}")
    print(f"Comunicação: {comunicacao}% | {status_com} |{descricao_com}")
    print(f"Bateria: {bateria}% | {status_bat} | {descricao_bat}")
    print(f"Oxigênio: {oxigenio}% | {status_oxi} | {descricao_oxi}")
    print(f"Estabilidade: {estabilidade}% | {status_est} | {descricao_est}")
    print()
    print(f"Pontuação de risco do ciclo: {risco_total}")
    print(f"Classificação: {classificar_ciclo(risco_total)}")
    print("\nAções executadas:")
    for acao in acoes:
        print("-", acao)
    print("\nRecomendação geral do ciclo:")
    print(recomendacao_geral(risco_total))

# Calculo da média de cada área de análise
media_temperatura = calcular_media(dados_missao, 0)
media_comunicacao = calcular_media(dados_missao, 1)
media_bateria = calcular_media(dados_missao, 2)
media_oxigenio = calcular_media(dados_missao, 3)
media_estabilidade = calcular_media(dados_missao, 4)

# Identificando o maior risco registrado de todos os ciclos
maior_risco = max(riscos_ciclos)

# Identificando a posição do maior risco registrado de todos os ciclos
ciclo_critico = riscos_ciclos.index(maior_risco) + 1

# Calculo do nível médio de risco da missão
risco_medio = sum(riscos_ciclos) / len(riscos_ciclos)

# Contador de ciclos críticos
quantidade_criticos = 0

for risco in riscos_ciclos:
    if risco >= 6:
        quantidade_criticos += 1

# Encontrar a área mais afetada
indice_area = pontuacao_areas.index(max(pontuacao_areas))
area_mais_afetada = areas_monitoradas[indice_area]

# Organização para exibição do relatório final da missão
print("\n")
print("=" * 60)
print("RELATÓRIO FINAL DA MISSÃO")
print("=" * 60)

print(f"Missão: {missao}")
print(f"Equipe: {equipe}")
print()
print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
print()
print(f"Média de temperatura: {media_temperatura:.2f}°C")
print(f"Média de comunicação: {media_comunicacao:.2f}%")
print(f"Média de bateria: {media_bateria:.2f}%")
print(f"Média de oxigênio: {media_oxigenio:.2f}%")
print(f"Média de estabilidade: {media_estabilidade:.2f}%")
print()
print(f"Ciclo mais crítico: Ciclo {ciclo_critico}")
print(f"Maior pontuação de risco: {maior_risco}")
print(f"Risco médio da missão: {risco_medio:.2f}")
print(f"Quantidade de ciclos críticos: {quantidade_criticos}")

print("\nTendência da missão:")
print(analisar_tendencia(riscos_ciclos))

print("\nPontuação acumulada por área:")

for i in range(len(areas_monitoradas)):
    print(f"{areas_monitoradas[i]}: {pontuacao_areas[i]} pontos")

print("\nÁrea mais afetada:")
print(area_mais_afetada)

print("\nClassificação final da missão:")

if risco_medio <= 2:
    print("MISSÃO ESTÁVEL")
elif risco_medio <= 5:
    print("MISSÃO EM ATENÇÃO")
else:
    print("MISSÃO CRÍTICA")

print("\nConclusão:")

# Missão passou por crise mas conseguiu se recuperar
if (
    quantidade_criticos > 0
    and riscos_ciclos[-1] < riscos_ciclos[ciclo_critico - 1]
    and riscos_ciclos[-1] <= 2
):

    print(
        f"A missão enfrentou uma situação crítica durante o "
        f"\nCiclo {ciclo_critico}, principalmente na área "
        f"\n'{area_mais_afetada}'. Após a execução das ações "
        f"\ncorretivas automáticas, os indicadores apresentaram "
        f"\nmelhora progressiva, permitindo a recuperação da "
        f"\noperação e a estabilização dos sistemas nos ciclos finais."
    )

# Houve melhora, mas ainda existem riscos
elif (
    quantidade_criticos > 0
    and riscos_ciclos[-1] < riscos_ciclos[ciclo_critico - 1]
):

    print(
        f"A missão apresentou momentos de instabilidade "
        f"\nsignificativa, atingindo seu maior nível de risco no "
        f"\nCiclo {ciclo_critico}. As ações implementadas pelo "
        f"\nMission Control AI contribuíram para reduzir os riscos "
        f"\noperacionais, porém a área '{area_mais_afetada}' "
        f"\nainda requer monitoramento contínuo para garantir a "
        f"\nplena recuperação da missão."
    )

# Missão piorou ao longo do tempo
elif riscos_ciclos[-1] > riscos_ciclos[0]:

    print(
        f"A análise dos ciclos indica deterioração gradual das "
        f"\ncondições operacionais da missão. Foram registrados "
        f"\n{quantidade_criticos} ciclos críticos e a área "
        f"\n'{area_mais_afetada}' apresentou o maior acúmulo de "
        f"\nalertas. Recomenda-se reforçar os protocolos de "
        f"\ncontingência e priorizar a recuperação dos sistemas "
        f"\nmais afetados."
    )

# Missão estável
else:

    print(
        f"A missão manteve comportamento estável durante os "
        f"\n{len(dados_missao)} ciclos analisados. Embora a área "
        f"\n'{area_mais_afetada}' tenha concentrado a maior parte "
        f"\ndos alertas registrados, os sistemas permaneceram "
        f"\ndentro dos limites operacionais esperados."
    )
