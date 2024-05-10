import streamlit as st

def main():
    

    # Embedding Dash app using iframe
    st.markdown(
        """
        <iframe src="http://localhost:8050/"  style="border: none; width: 1000px; height: 800px;  "></iframe>
        """,
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()
