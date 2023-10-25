# Paper Similarity Search with Streamlit and Weaviate

This repository contains an application designed to recommend scientific papers that are most similar to a given input paragraph. The application uses the `llama` and `weaviate` libraries to achieve this. For ease of deployment, a `docker-compose.yml` file is provided to run Weaviate in a container since native installation on Windows posed challenges.

## Table of Contents
- [Methodology](#methodology)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [Notebook Approach](#notebook-approach)
- [Contributing](#contributing)

## Methodology
1. **Data Indexing**: The application begins by reading scientific papers from a designated bucket and indexing them using Weaviate. The data is read using the `SimpleDirectoryReader` and parsed into nodes with the `SimpleNodeParser`.
2. **Vector Database Creation**: Each node (paper or extracted text) is transformed into a vector using Weaviate's capabilities.
3. **Querying**: On inputting a paper's paragraph, the application queries the vector database to get the top 3 most similar papers.
4. **Output Presentation**: The titles and summaries of the top 3 papers are presented to the user.

## Setup and Installation

### Prerequisites
- Docker
- Python 3.x

### Steps
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/fshnkarimi/Similar-Paper-Reccomendation.git
    cd Similar-Paper-Reccomendation
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Weaviate with Docker**:
   If you're on Windows or facing issues with Weaviate's native installation, the provided `docker-compose.yml` makes it easy to run Weaviate in a Docker container.
    ```bash
    docker-compose up -d
    ```

## Running the Application
1. **Start the Streamlit App**:
    ```bash
    streamlit run app.py
    ```

2. Visit the URL shown in the terminal to interact with the application.

3. Input a paragraph from a scientific paper and get recommendations!

## Notebook Approach
If you'd rather see the step-by-step breakdown of the entire application along with the corresponding outputs, you can use the Jupyter Notebook:
1. Navigate to the `notebooks` directory:
    ```bash
    cd notebooks
    ```

2. Start Jupyter:
    ```bash
    jupyter notebook
    ```

3. Open the provided notebook and execute the cells in sequence.

![Demo GIF](DemoVid.gif)


