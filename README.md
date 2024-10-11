# Benchmarking

Este projeto é um benchmark em Python que compara o desempenho de diferentes abordagens de concorrência — `threads`, `process` e `asyncio` — em dois tipos de tarefas: operações IO-bound (requisições HTTP) e CPU-bound (processamento matemático). O objetivo é avaliar qual dessas técnicas é mais eficiente em diferentes cenários de uso, proporcionando uma análise clara do desempenho relativo de cada abordagem em tarefas intensivas de entrada/saída e processamento de CPU.

## Requisição HTTP (IO-bound)

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

## Conclusão
