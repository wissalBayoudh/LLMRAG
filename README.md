# AgenticRAG Exploration and Testing

This repository contains Jupyter Notebook (`.ipynb`) files and Python (`.py`) scripts for exploring, learning, and testing **AgenticRAG** using the following libraries:

- **Langchain**
- **Chroma** for vector store embeddings
- **FastEmbedEmbeddings** for embedding creation
- **Tavily** for web search functionality

## Project Future Structure
AgenticRAG/
├── .ipynb files/
│   ├── example1.ipynb
│   └── example2.ipynb
├── .py files/
│   ├── llm_router.py
│   ├── generation_chain.py
│   ├── retrieval_grader.py
│   ├── hallucination_grader.py
│   ├── answer_grader.py
│   └── web_search_tool.py
├── requirements.txt
├── README.md
└── graph_result.png  # Image of the graph result


## LangGraph Workflow

### 1. LLM Router
- Implement the LLM router to direct requests to appropriate language models based on input criteria.

### 2. Generation Chain
- Create a chain for generating responses using the chosen LLM.

### 3. Retrieval Grader
- Implement the retrieval grader to evaluate the quality and relevance of retrieved information.

### 4. Hallucination Grader
- Develop a grader that assesses the likelihood of hallucinations in the generated outputs.

### 5. Answer Grader
- Create an answer grader to evaluate the correctness and usefulness of the final answers provided.

### 6. Web Search Tool (Tavily)
- Integrate the Tavily web search tool to enhance the capability of the LLM by retrieving information from the web.

## Graph Result

![Graph Result](graph_result.png)
#### Usage
Clone the repository:
```
git clone https://github.com/wissalBayoudh/LLMRAG.git
```
###### Installation

To install the required libraries, run:

```bash
pip install -r requirements.txt
```

