# Benchmarking

Este projeto é um benchmark em Python que compara o desempenho de diferentes abordagens de concorrência — `threads`, `process` e `asyncio` — em dois tipos de tarefas: operações IO-bound (requisições HTTP) e CPU-bound (processamento matemático). O objetivo é avaliar qual dessas técnicas é mais eficiente em diferentes cenários de uso, proporcionando uma análise clara do desempenho relativo de cada abordagem em tarefas intensivas de entrada/saída e processamento de CPU.

## Requisição HTTP (IO-bound)
In synchronous approach, execution took 302.84740805625916 seconds

Using processes, execution took 103.39325308799744 seconds
Using process pool (default workers), execution took 85.06695365905762 seconds
Using process pool (20 workers), execution took 79.38548803329468 seconds
Using process pool (10 workers), execution took 76.9515130519867 seconds

Using threads, execution took 70.77761507034302 seconds
Using threads with pool (default workers), execution took 74.92019581794739 seconds
Using threads with pool (20 workers), execution took 74.98805928230286 seconds
Using threads with pool (10 workers), execution took 77.3211715221405 seconds

With asyncio, execution took 2.2547695636749268 seconds

## Processamento Matemático (CPU-bound)

## Conclusão
