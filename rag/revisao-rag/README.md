# 📚 Revisão Prática de RAG

Este diretório contém um projeto prático de **RAG (Retrieval-Augmented Generation)**, desenvolvido para consolidar os conceitos de carregamento de documentos, chunking, vetorização e geração de respostas contextualizadas usando LangChain e modelos da Google (Gemini).

## 🎯 Objetivo

Demonstrar o fluxo completo de um sistema RAG:

1. Ingerir documentos PDF de uma pasta local.
2. Dividir o texto em chunks otimizados.
3. Vetorizar e armazenar no ChromaDB.
4. Recuperar os trechos mais relevantes e gerar respostas precisas usando um LLM.

---

## 🧪 Base de conhecimento da demonstração

Como prova de conceito, usei **meu próprio currículo (PDF gerado pela plataforma Gupy)** como base de conhecimento.

Assim, o agente consegue responder perguntas como:

- "Quando ele estudou Excel?"
- "Em qual instituição fez o curso?"
- "Quais cursos de IA foram concluídos?"
- "Qual foi sua experiência no Machado Meyer?"

Isso demonstra na prática o poder do RAG para consultar documentos privados sem enviar dados para treinamento do modelo.

---

## 🔄 Fluxo de Funcionamento

O projeto é dividido em dois scripts que representam as duas fases de um sistema RAG:

### 1. Fase de Indexação (`db.py`)

- **Carregamento:** lê os PDFs da pasta `base/` com `PyPDFDirectoryLoader`.
- **Chunking:** divide os documentos em chunks de 2000 caracteres com sobreposição de 400 (`RecursiveCharacterTextSplitter`).
- **Vetorização:** gera embeddings com o modelo `gemini-embedding-2` da Google.
- **Armazenamento:** persiste os vetores no ChromaDB (pasta `db/`).

### 2. Fase de Recuperação (`main.py`)

- **Busca:** recebe a pergunta via terminal e faz `similarity_search_with_relevance_scores` no ChromaDB, recuperando os 4 chunks mais relevantes.
- **Filtro de Relevância:** verifica se o score é maior ou igual a `0.5`. Se for baixo, avisa que não encontrou informações (evitando alucinações).
- **Geração:** monta o prompt com a pergunta + contexto e envia para o **Gemini Flash**.

---

## 🛠️ Stack Tecnológica

| Categoria | Tecnologias |
|---|---|
| **Linguagem** | Python 3.10+ |
| **Orquestração** | LangChain, LangChain Core |
| **Banco Vetorial** | ChromaDB |
| **Modelos** | Google Gemini |
| **Processamento** | pypdf, python-dotenv |

---

## ⚙️ Como Executar o Projeto

### 1. Pré-requisitos

- Python 3.10 ou superior instalado.
- Uma **API Key do Google Gemini** (obtida no [Google AI Studio](https://aistudio.google.com/)).

### 2. Instalação

Navegue até esta pasta no terminal:

```bash
# Ambiente virtual (Windows)
python -m venv .venv
.venv\Scripts\activate

# Ambiente virtual (Linux/Mac)
python3 -m venv .venv
source .venv/bin/activate

# Dependências
pip install -r requirements.txt
```

### 3. Configurar variáveis de ambiente

Crie um arquivo `.env` nesta pasta:

```
GOOGLE_API_KEY=sua_chave_aqui
```

### 4. Criar o banco vetorial

Coloque seus PDFs na pasta `base/` e rode:

```bash
python db.py
```

### 5. Perguntar ao sistema

```bash
python main.py
```

---

## 📸 Demonstração

**Pergunta:** "quando ele estudou excel? e foi em qual instituição?"

![Pergunta no terminal](docs/print_pergunta.png)

**Resposta da IA:** Fundação Bradesco (curso Microsoft Excel 2016 - Intermediário), com verificação emitida em fevereiro de 2024. ✅

![Resposta da IA](docs/print_resposta.png)

---

## 📁 Estrutura de Arquivos

```
revisao-rag/
├── base/    # PDFs (currículo Gupy)
├── db/      # banco vetorial ChromaDB
├── docs/    # prints da demonstração
├── db.py    # script de indexação
├── main.py  # script de consulta
├── requirements.txt
└── README.md
```

---

## 💡 Aprendizados e Próximos Passos

- **Aprendizado:** pipeline completo de RAG, importância do `chunk_overlap` para manter contexto e uso de `relevance_scores` para filtrar respostas quando a base não possui a informação.
- **Próximas evoluções:** histórico de conversa (memória), novas estratégias de chunking (por sentenças, markdown) e suporte a múltiplos formatos (CSV, TXT).

---

**Herick Carvalho** — [LinkedIn](https://www.linkedin.com/in/herickcarv) | [GitHub](https://github.com/herick-oak)
