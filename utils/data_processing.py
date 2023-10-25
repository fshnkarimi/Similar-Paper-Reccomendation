from llama_index import SimpleDirectoryReader
from llama_index.node_parser import SimpleNodeParser

def process_and_index_data(bucket_path='./data'):
    """
    Processes and indexes the data from the provided bucket path.

    Args:
    - bucket_path (str): The path to the directory containing the paper data. 
                         Default is './data'.

    Returns:
    - list: A list of nodes representing the indexed data from the documents.

    Example:
    >>> nodes = process_and_index_data('./data')
    >>> type(nodes)
    <class 'list'>
    """

    # Load papers from the provided path
    papers = SimpleDirectoryReader(bucket_path).load_data()

    # Parse the papers into nodes with specified chunk size and overlap
    parser = SimpleNodeParser.from_defaults(chunk_size=1024, chunk_overlap=20)
    nodes = parser.get_nodes_from_documents(papers)

    return nodes
