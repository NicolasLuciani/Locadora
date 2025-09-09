# 🎬 Sistema de Locadora

### Um sistema simples de locadora de filmes e jogos, desenvolvido em Python para praticar Programação Orientada a Objetos (POO).

---

## 🚀 Funcionalidades
- Cadastrar clientes (com nome e CPF)
- Cadastrar filmes (com título, gênero e duração)
- Cadastrar jogos (com título, plataforma e faixa etária)
- Listar clientes, filmes e jogos
- Locar e devolver itens

---

## 📂 Estrutura do Projeto

- **app.py**  
  Menu principal que chama as funções utilizando `match case`, deixando o código mais organizado.

- **classes.py**  
  Contém as classes principais do sistema:  
  - `Item` → classe base para filmes e jogos  
  - `Filme` → herda de Item e adiciona gênero e duração  
  - `Jogo` → herda de Item e adiciona plataforma e faixa etária  
  - `Cliente` → representa os clientes, com nome, CPF e itens locados  
  - `Locadora` → gerencia os clientes e os itens  

- **funcoes.py**  
  Funções auxiliares para o sistema:  
  - `cadastrar_clientes()`  
  - `cadastrar_filmes()`  
  - `cadastrar_jogos()`  
  - `cadastrar_filmes_ou_jogos()`  
  - `listar()`  
  - `listar_clientes()`  
  - `listar_filmes()`  
  - `listar_jogos()`  
---

# Código 'classes.py'

```python

```
