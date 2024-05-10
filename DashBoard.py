import streamlit as st
from test_backup import app  # Import your Dash app object

def main():
    # Title of your app
    st.title("Placement Analytics Dashboard")

    # Run your Dash app within Streamlit
    app.run_server(port=8001)

if __name__ == "__main__":
    main()