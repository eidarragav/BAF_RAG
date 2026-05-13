from langchain_community.document_loaders import PyMuPDFLoader, DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

from config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL, CHROMA_DIR, PDF_DIR

def ingest():
    print("Cargando PDFs...")

    loader = DirectoryLoader(
        PDF_DIR,
        glob="**/*.pdf",
        loader_cls=PyMuPDFLoader
    )

    documents = loader.load()

    print(f"Documentos cargados: {len(documents)}")

    # Dividir texto
    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    texts = splitter.split_documents(documents)

    print(f"Chunks generados: {len(texts)}")

    # Embeddings
    embeddings = OpenAIEmbeddings(
        openai_api_key=OPENROUTER_API_KEY,
        openai_api_base=OPENROUTER_BASE_URL
    )

    # Crear DB
    db = Chroma.from_documents(
        texts,
        embeddings,
        persist_directory=CHROMA_DIR
    )

    db.persist()

    print("Base vectorial creada correctamente.")

if __name__ == "__main__":
    ingest()