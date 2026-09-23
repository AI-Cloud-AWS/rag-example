RAG Example 

----

**Retrieval-Augmented Generation (RAG) system in Python** from scratch.

**What is RAG (Retrieval-Augmented Generation)?**

Instead of asking an LLM to answer entirely from its training data, you first retrieve relevant information from your own documents and put that information into the prompt.

This system demonstrates a simple implementation of RAG. It shows the steps on how to:

1. Load documents.

2. Split them into chunks.

3. Convert chunks into embeddings.

4. Store those embeddings in a vector database.

5. Retrieve the most relevant chunks for a question.

6. Give those chunks to an LLM to generate an answer.



**Important**: In order to execute this example,

- to install the dependencies in requirements.txt

- you also nee OpenAI key 





