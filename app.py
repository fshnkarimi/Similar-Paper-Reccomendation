import streamlit as st
from utils import config, data_processing, index_utils
import time


# Streamlit UI setup
st.title("Similar Paper Recommendation System")

# Initialization
client = index_utils.setup_weaviate_client()
nodes = data_processing.process_and_index_data(config.BUCKET_PATH)
index = index_utils.setup_vector_index(client, nodes)

input_paragraph = st.text_area("Input a paragraph for recommendations:", "")


if st.button('Get Recommendations'):
    if input_paragraph:
        
        # Display spinner while fetching results
        with st.spinner('Fetching recommendations...'):
            
            # Progress bar for user's visual cue
            latest_iteration = st.empty()
            bar = st.progress(0)

            for i in range(100):
                latest_iteration.text(f'Progress {i+1}%')
                bar.progress(i + 1)
                time.sleep(0.1)  
            
            # Create a query engine and fetch results
            query_engine = index.as_query_engine()
            response = query_engine.query(f"give the titles and 1 sentence summary for each of the top 3 most similar papers in the database to this paragraph: {input_paragraph}")
            st.write(response.response)
            
    else:
        st.warning('Please input a paragraph.')