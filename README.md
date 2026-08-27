# Theory of Graphs — Path Finder (Algoritmo de Dijkstra)

🚀 Bem-vindo ao Path Finder — uma pequena aplicação interativa que demonstra o algoritmo de Dijkstra em uma grade (grid) ponderada.  
Selecione um ponto de partida e um destino e veja o algoritmo encontrar caminhos eficientes entre eles.

---

## Visão geral
Este projeto tem por objetivo:
- Visualizar como o algoritmo de Dijkstra explora um grafo/grade.
- Demonstrar caminhos alternativos (variantes simples de K-caminhos) bloqueando arestas para forçar rotas diferentes.
- Servir como base didática para estudar algoritmos de caminhos mínimos e exploração de grafos.

A aplicação é dividida em frontend (visualização interativa) e backend (cálculo do caminho).

---

## Recursos
- Interface web com uma grade 8x8 para selecionar start / goal.
- Backend em Flask expondo um endpoint `/shortest-path`.
- Implementação simples do Dijkstra que suporta gerar múltiplos caminhos ao bloquear arestas da solução anterior.
- Código organizado (backend/frontend) para facilitar extensões.

---

## Demonstração rápida
1. Execute o servidor Flask.
2. Abra `http://localhost:5000` no navegador.
3. Clique nas células para definir o start e o goal.
4. Clique em "Encontrar Caminho" para visualizar o(s) caminho(s) retornado(s).

(Adicionar um GIF ou screenshot aqui melhora muito a apresentação — vale a pena incluir um.)

---

## Instalação e execução local

Recomendado: criar um virtualenv

1. Clonar o repositório:
   git clone https://github.com/PontesDiogo/Theory-of-graphs.git
2. Entrar na pasta:
   cd Theory-of-graphs
3. Criar e ativar virtualenv (opcional mas recomendado):
   python -m venv venv
   source venv/bin/activate  # macOS / Linux
   venv\Scripts\activate     # Windows
4. Instalar dependências:
   pip install Flask
5. Iniciar o servidor:
   python backend/app.py
6. Abrir no navegador:
   http://localhost:5000

---

## API
Endpoint principal:
- POST `/shortest-path`
  - Recebe JSON: { "start": [x, y], "goal": [x, y] }
  - Retorna: { "paths": [ [...], [...], ... ] } — lista de caminhos (cada caminho é uma lista de coordenadas)

Exemplo de chamada com curl:
curl -X POST -H "Content-Type: application/json" -d '{"start":[0,0],"goal":[7,7]}' http://localhost:5000/shortest-path

---

## Estrutura do projeto
- backend/
  - app.py        — servidor Flask e rota `/shortest-path`
  - dijkstra.py   — implementação do algoritmo
- frontend/
  - templates/index.html
  - static/js/*
  - static/css/*
- README.md

---

## Sobre a implementação do algoritmo
O backend usa uma versão clássica do Dijkstra (com heap) para grade 4-direcional (cima/baixo/esquerda/direita).  
Para gerar múltiplos caminhos (parciais "k-caminhos"), o algoritmo encontrado bloqueia a primeira aresta do caminho anterior e recalcula, produzindo rotas alternativas simples. Isso não é a abordagem formal de "k-shortest paths" (como Yen), mas funciona como demonstração didática.

Possíveis melhorias:
- Suporte a pesos diferentes por célula/aresta.
- Implementar algoritmo de k-shortest paths (Yen) para caminhos distintos reais.
- Mostrar visualmente as distâncias/priority queue enquanto o algoritmo executa (animação passo-a-passo).

---

## Contribuições
Contribuições são bem-vindas! Sugestões:
- Tornar a grade configurável (tamanho, obstáculos, pesos).
- Adicionar testes unitários para o módulo dijkstra.py.
- Melhorar a UI/UX (animações, legendas, exportação de resultados).

Se quiser, abra uma issue descrevendo a melhoria ou envie um pull request.

---

## Contato
Para entrar em contato ou contribuir, use uma das opções abaixo:

- GitHub: [@PontesDiogo](https://github.com/PontesDiogo)
- Issues do repositório (relatar bugs / pedir features): https://github.com/PontesDiogo/Theory-of-graphs/issues
- Pull requests (envie contribuições): https://github.com/PontesDiogo/Theory-of-graphs/pulls
- Email: [diogogpontes@gmail.com](mailto:diogogpontes@gmail.com)
- LinkedIn: https://www.linkedin.com/in/diogogarciapontes/

Dica: use *Issues* para bugs e pedidos de funcionalidades; abra *Pull Requests* para enviar código.

---

## Sugestões para o README (opcional)
- Incluir screenshots ou um GIF curto da aplicação em funcionamento.
- Adicionar um arquivo LICENSE (por exemplo MIT) se quiser tornar o uso público.
- Incluir instruções para deploy (Heroku / Railway / Vercel + backend).

---

## Contato rápido
Criado por PontesDiogo — sinta-se à vontade para abrir issues ou pull requests.

