# Mission Control AI
## Sistema Inteligente de Monitoramento para Missões Espaciais

### Global Solution 2026.1
**Disciplina:** Pensamento Computacional e Automação com Python

---

## Integrantes

| Nome | RM |
|--------|--------|
| Kauanne Paula de Oliveira | 574191 |
| Nayhely Estela Calle Castillo | 571416 |

---

## Sobre o Projeto

O **Mission Control AI** é um sistema desenvolvido para auxiliar no monitoramento de missões espaciais por meio da análise contínua dos principais indicadores operacionais de uma nave.

A solução simula o funcionamento de um centro de controle automatizado capaz de:

- Monitorar os sistemas da missão em ciclos sucessivos;
- Detectar situações de atenção e criticidade;
- Calcular o nível de risco operacional;
- Executar ações corretivas automáticas;
- Gerar recomendações para os operadores;
- Avaliar tendências da missão ao longo do tempo;
- Produzir relatórios completos de desempenho.

O projeto foi desenvolvido utilizando conceitos fundamentais de Python, incluindo:

- Matrizes
- Listas
- Estruturas condicionais
- Estruturas de repetição
- Funções
- Manipulação de dados
- Geração de relatórios

---

## Objetivo

Desenvolver um sistema capaz de identificar problemas operacionais em uma missão espacial e auxiliar na tomada de decisões por meio de análises automatizadas.

O sistema busca simular cenários reais em que falhas de comunicação, energia, temperatura, oxigênio e estabilidade podem comprometer o sucesso da missão.

---

## Indicadores Monitorados

Cada ciclo da missão possui cinco parâmetros principais:

| Indicador | Descrição |
|------------|------------|
| Temperatura | Temperatura interna da nave (°C) |
| Comunicação | Qualidade do sinal de comunicação (%) |
| Bateria | Nível de energia disponível (%) |
| Oxigênio | Nível de oxigênio disponível (%) |
| Estabilidade | Estabilidade geral dos sistemas (%) |

Estrutura utilizada:

```python
[
    temperatura,
    comunicacao,
    bateria,
    oxigenio,
    estabilidade
]
```

---

## Critérios de Avaliação

### Temperatura

| Faixa | Status |
|---------|---------|
| 18°C a 30°C | Normal |
| 31°C a 35°C | Atenção |
| >35°C | Crítico |

### Comunicação

| Faixa | Status |
|---------|---------|
| ≥60% | Normal |
| 30% a 59% | Atenção |
| <30% | Crítico |

### Bateria

| Faixa | Status |
|---------|---------|
| ≥50% | Normal |
| 20% a 49% | Atenção |
| <20% | Crítico |

### Oxigênio

| Faixa | Status |
|---------|---------|
| ≥90% | Normal |
| 80% a 89% | Atenção |
| <80% | Crítico |

### Estabilidade

| Faixa | Status |
|---------|---------|
| ≥70% | Normal |
| 40% a 69% | Atenção |
| <40% | Crítico |

---

## Sistema de Pontuação de Risco

Cada indicador recebe uma pontuação:

| Status | Pontos |
|---------|---------|
| Normal | 0 |
| Atenção | 1 |
| Crítico | 2 |

A soma dos pontos gera o risco total do ciclo.

### Classificação da Missão

| Pontuação Total | Classificação |
|-----------------|---------------|
| 0 a 2 | Missão Estável |
| 3 a 5 | Missão em Atenção |
| 6 a 10 | Missão Crítica |

---

## Ações Automáticas

Quando uma condição de risco é detectada, o sistema simula ações corretivas.

Exemplos:

### Temperatura

- Ativação do sistema de resfriamento emergencial
- Ajuste preventivo do controle térmico

### Comunicação

- Recalibração de antenas
- Restabelecimento do sinal

### Bateria

- Ativação do modo de economia de energia
- Redução preventiva do consumo energético

### Oxigênio

- Ajuste dos reservatórios
- Acionamento do protocolo de suporte à vida

### Estabilidade

- Aplicação de correções preventivas
- Suspensão de operações secundárias

---

## Funcionalidades Implementadas

O sistema realiza automaticamente:

### Análise individual dos indicadores

- Temperatura
- Comunicação
- Bateria
- Oxigênio
- Estabilidade

### Análise dos ciclos

- Cálculo do risco total
- Classificação do ciclo
- Recomendações operacionais

---

## Análise de Tendência da Missão

Além da classificação individual de cada ciclo, o sistema realiza uma análise da evolução da missão ao longo do tempo.

Para isso, é comparado o maior nível de risco registrado durante a operação com o risco observado no último ciclo monitorado.

### Critérios utilizados

| Situação | Resultado |
|-----------|------------|
| Último risco menor que o maior risco registrado | Recuperação após período crítico |
| Último risco igual ao maior risco registrado | Missão permanece em estado crítico |
| Último risco superior ao maior risco registrado | Risco crescente |

### Relatório Final

- Médias dos indicadores
- Ciclo mais crítico
- Maior risco registrado
- Quantidade de ciclos críticos
- Tendência da missão
- Área mais afetada
- Classificação final
- Conclusão automática

---

## Cenário Simulado

A missão foi construída para representar um cenário realista de degradação gradual dos sistemas seguida por uma recuperação progressiva.

### Evolução da Missão

| Ciclo | Situação |
|---------|---------|
| 1 | Estável |
| 2 | Pequena degradação |
| 3 | Atenção inicial |
| 4 | Atenção |
| 5 | Próximo do crítico |
| 6 | Crítico |
| 7 | Recuperação inicial |
| 8 | Recuperação consistente |

Esse comportamento permite avaliar a capacidade do sistema em detectar problemas e aplicar ações corretivas ao longo da operação.

---

## Tecnologias Utilizadas

- Python 3
- Estruturas de dados (listas e matrizes)
- Funções
- Estruturas condicionais
- Estruturas de repetição

---

## Como Executar

1. Instale o Python 3.
2. Baixe o arquivo `mission_control.py`.
3. Execute o comando:

```bash
python mission_control.py
```

ou

```bash
python3 mission_control.py
```

---

## Exemplo de Saída

O sistema exibe:

- Status detalhado de cada ciclo;
- Ações executadas automaticamente;
- Recomendações operacionais;
- Análise da tendência da missão;
- Relatório final consolidado da missão.

---

## Considerações Finais

O Mission Control AI demonstra como conceitos fundamentais de programação podem ser aplicados na criação de sistemas inteligentes de apoio à decisão.

Por meio da análise automatizada dos indicadores da missão, o sistema é capaz de identificar riscos, sugerir ações corretivas e acompanhar a evolução operacional dos sistemas monitorados, contribuindo para a segurança e o sucesso da missão espacial.
