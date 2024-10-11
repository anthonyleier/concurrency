# Benchmarking

Este projeto é um benchmark em Python que compara o desempenho de diferentes abordagens de concorrência — `threads`, `process` e `asyncio` — em dois tipos de tarefas: operações IO-bound (requisições HTTP) e CPU-bound (processamento matemático). O objetivo é avaliar qual dessas técnicas é mais eficiente em diferentes cenários de uso, proporcionando uma análise clara do desempenho relativo de cada abordagem em tarefas intensivas de entrada/saída e processamento de CPU.

## Requisição HTTP (IO-bound)
In synchronous approach, execution took 302.84740805625916 seconds

Using processes, execution took 103.39325308799744 seconds
Using process pool (default workers), execution took 85.06695365905762 seconds
Using process pool (20 workers), execution took 79.38548803329468 seconds
Using process pool (10 workers), execution took 76.9515130519867 seconds



## Processamento Matemático (CPU-bound)

## Conclusão
