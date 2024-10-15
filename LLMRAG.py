from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
# Embed and store
from langchain.vectorstores import FAISS
from langchain.embeddings import OllamaEmbeddings
from langchain.llms import Ollama


     
def main():
    loader = DirectoryLoader("./docs")
    data = loader.load()
    # Split ino chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=100)
    all_splits = text_splitter.split_documents(data)
    print(f"Split into {len(all_splits)} chunks")
    vectorstore = FAISS.from_documents(documents=all_splits,
    embedding=OllamaEmbeddings())
    print(f"Loaded {len(data)} documents")
    # RAG prompt
from langchain import hub
QA_CHAIN_PROMPT = hub.pull("rlm/rag-prompt-llama")
# LLM
llm = Ollama(model="llama2:13b",
verbose=True,
callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)
print(f"Loaded LLM model {llm.model}")
# QA chain
from langchain.chains import RetrievalQA
qa_chain = RetrievalQA.from_chain_type(
llm,
retriever=vectorstore.as_retriever(),
chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
)
# Ask a question
question = """ KEEP THE TEXT AS IT IS, CHANGE ONLY THE LAYOUT 
Organize the layout of the transcript, DO NOT refomulate the text
Preserve the complete and original text
Structure the layout: Use clear headings, subheadings..
DO NOT summarize, Do NOT USE BULLET POINTS.
make it appealing by using emojies and titles to each part of the transcript 
Here's the transcript transcription text :
"{data}"
"""
result = qa_chain({"query": question})
#print(f"Output:\n{result['result']}")
if __name__ == "__main__":
    main()