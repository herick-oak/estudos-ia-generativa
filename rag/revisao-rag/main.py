from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()

CAMINHO_DB = "db"


prompt_templete = """
Responda a pergunta do Usuario:
{pergunta}
Com base nessas informações abaixo:
{base_conhecimento}
"""

def perguntar():
    pergunta = input("Escreva sua pergunta: ")

    # Carregar banco de dados
    funcao_embedding = embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2"
        )

    db = Chroma(persist_directory=CAMINHO_DB,embedding_function=funcao_embedding)

    # comparar a pergunta do usuario e passar para o embedding com o banco de dados

    resultados = db.similarity_search_with_relevance_scores(pergunta, k=4)

    if len(resultados) == 0 or resultados[0][1] < 0.5:
        print("Não conseguiu encontrar um resultado na base de conhecimento.")
        return

    textos_resultados = []
    for resultado in resultados:
        texto = resultado[0].page_content
        textos_resultados.append(texto)

    base_conhecimento = "\n\n----\n\n".join(textos_resultados)

    prompt = ChatPromptTemplate.from_template(prompt_templete)  
    prompt = prompt.invoke({"pergunta":pergunta,"base_conhecimento":base_conhecimento})

    modelo = GoogleGenerativeAI(model="gemini-3.6-flash")

    texto_resposta = modelo.invoke(prompt)
    print("Resposta da I.A:", texto_resposta)

perguntar()

