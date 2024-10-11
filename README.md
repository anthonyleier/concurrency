# Benchmarking

Este projeto é um benchmark em Python que compara o desempenho de diferentes abordagens de concorrência — `threads`, `process` e `asyncio` — em dois tipos de tarefas: operações IO-bound (requisições HTTP) e CPU-bound (processamento matemático). O objetivo é avaliar qual dessas técnicas é mais eficiente em diferentes cenários de uso, proporcionando uma análise clara do desempenho relativo de cada abordagem em tarefas intensivas de entrada/saída e processamento de CPU.

## Requisição HTTP (IO-bound)

O teste de performance mede o tempo de execução de uma tarefa que envolve download de dados e gravação de arquivos. Para esto, é realizado o download dos sprites (imagens) de 255 Pokémons usando a API do PokeAPI e gravando cada imagem com seu respectivo nome no disco. Como é uma operação que envolve a comunicação de rede, está atrealada ao uso de dados de entrada e saída, gerando IO-bound.

| Abordagem                      | Tempo de execução |
|--------------------------------|-------------------|
| Síncrona                       | 302.84 segundos   |
| Processes                      | 103.39 segundos   |
| Process Pool (Default Workers) | 85.06 segundos    |
| Process Pool (20 Workers)      | 79.38 segundos    |
| Process Pool (10 Workers)      | 76.95 segundos    |
| Threads                        | 70.77 segundos    |
| Threads Pool (Default Workers) | 74.92 segundos    |
| Threads Pool (20 Workers)      | 74.98 segundos    |
| Threads Pool (10 Workers)      | 77.32 segundos    |
| Asyncio com Aiohttp            | 2.25 segundos     |

## Processamento Matemático (CPU-bound)

O teste de performance mede o tempo de execução para contar números primos dentro de um intervalo de 0 a 10 milhões. A função `count_primes_in_range` percorre cada número dentro do intervalo e usa a função `is_prime` para verificar se o número é primo. O teste mede o tempo total necessário para realizar essa contagem e imprime a duração juntamente com o número de primos encontrados. O objetivo é avaliar o desempenho de um cálculo intensivo em CPU.

| Abordagem                      | Tempo de execução |
|--------------------------------|-------------------|
| Síncrona                       | 96.39 segundos    |
| Threads                        | 93.60 segundos    |
| Processos                      | 32.16 segundos    |
| Asyncio                        | 95.55 segundos    |

## Conclusão

Percebe-se que o uso de concorrência em Python proporciona muitos ganhos de desempenho. No cenário `IO-bound`, como o teste de requisição HTTP, o `asyncio` com `aiohttp` foi o grande vencedor, com um tempo de execução significativamente menor (2.25 segundos). Isso ocorre porque `asyncio` lida muito bem com operações de entrada/saída não bloqueantes, maximizando a eficiência ao permitir que o código continue a ser executado enquanto aguarda respostas de rede.

Já no cenário `CPU-bound`, o `multiprocessing` se destacou, com a abordagem de processos sendo muito mais eficiente (32.16 segundos) que threads ou async. O motivo é que tarefas intensivas em CPU se beneficiam da separação em múltiplos processos, já que cada processo roda em um core separado, permitindo o paralelismo real e não sendo limitado pelo GIL (Global Interpreter Lock) do Python, como acontece com `threads` e `asyncio`.

Portanto, para maximizar os ganhos de desempenho, é essencial escolher a abordagem correta de acordo com o tipo de tarefa. Para IO-bound, `asyncio` oferece os melhores resultados, seguido pelo `threading` enquanto para tarefas CPU-bound, a abordagem de multiprocessing com processos se mostra mais eficiente.
