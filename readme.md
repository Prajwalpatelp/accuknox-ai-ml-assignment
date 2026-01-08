# AI/ML Assignment Repository

This repository contains solutions for two assignments focusing on **Python programming, API data handling, database operations, data visualization, and AI/ML concepts**.

### Problem Statement 1
1. **API Data Retrieval and Storage**  
   - Fetch data from an external REST API providing a list of books in JSON format with attributes like `title`, `author`, and `publication_year`.
   - Store the retrieved data into a local **SQLite database**.
   - Display the stored data.

2. **Data Processing and Visualization**  
   - Fetch a dataset containing students' test scores from an API.
   - Calculate the **average score** for each student.
   - Create a **bar chart** to visualize the scores.
   - The computed average test score across all students is **84.88**.
   ![Bar chart for students scores ](bar_chart_iamge.png)


3. **CSV Data Import to a Database**  
   - Read data from a CSV file containing user information (`name`, `email`).
   - Insert the data into a **SQLite database**.

---

### Assignment 1 Flowchart

```mermaid
flowchart TD
    A[Start] --> B[API Data Retrieval]
    B --> C[Store Data in SQLite]
    C --> D[Data Processing (Calculate Avg Score)]
    D --> E[Data Visualization (Bar Chart)]
    C --> F[CSV Data Import to SQLite]
    F --> G[End]
```

### Problem Statement 2
# Problem Statement-2 – Approach Flowchart

```mermaid
flowchart TD
    A[Start] --> B[Self-Assessment of Skills<br/>(LLM, DL, AI, ML)]
    B --> C[Identify Strengths & Learning Areas]
    C --> D[Study LLM System Architecture]
    D --> E[Define Chatbot Components<br/>(UI, Backend, LLM, Knowledge)]
    E --> F[Understand Vector Embeddings]
    F --> G[Select Vector Database<br/>(FAISS)]
    G --> H[Map Use Case to Architecture<br/>(Customer Support Chatbot)]
    H --> I[Summarize Learnings & Insights]
    I --> J[End]
```