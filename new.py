import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

# Load data from direct URLs to raw CSV files
data_url1 = 'Placement Statistics-2023.csv'
df2023 = pd.read_csv(data_url1)
data_url2 = 'Placement Statistics-2022.csv'
df2022 = pd.read_csv(data_url2)
data_url3 = 'Placement Statistics-2021.csv'
df2021 = pd.read_csv(data_url3)
data_url4 = 'Placement Statistics-2020.csv'
df2020 = pd.read_csv(data_url4)
data_url5 = 'Placement Statistics-2019.csv'
df2019 = pd.read_csv(data_url5)

def main():
    st.title('Placement Dashboard')

    st.sidebar.image("https://jssaten.ac.in//assets/images/logo/jsslogoicon.png", width=150)
    st.sidebar.title('Navigation')
    page = st.sidebar.radio("Go to", ["Home", "AvgGraph", "2023", "2022", "2021", "2020", "2019"])

    if page == "Home":
        st.header('Welcome to the Placement Dashboard')
        st.write("This dashboard provides insights into the placement statistics of the institution.")
        st.write("Use the navigation sidebar to explore different sections.")

    elif page == "AvgGraph":
        st.header('Average Salary Over the Years')
        avg_salary_list = [6.76, 7.07, 5.05, 5.46, 4.2]
        year_list = [2023, 2022, 2021, 2020, 2019]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=year_list, y=avg_salary_list, name='Average Salary', marker_color='royalblue'))
        fig.update_layout(xaxis_title='Year', yaxis_title='Average Salary')
        st.plotly_chart(fig)

    elif page in ["2023", "2022", "2021", "2020", "2019"]:
        year = int(page)
        df_year = globals()[f"df{year}"]  # Get DataFrame dynamically
        st.header(f'Placement Statistics for {year}')

        col1, col2, col3, col4 = st.columns(4)  # Create 4 columns

        with col1:
            st.markdown(
                "<div style='padding: 10px; border-radius: 10px; background-color: #4040FF; "
                "height: 150px;'>"
                "<h3 style='text-align: center;'>Companies Visited</h3>"
                "<p style='text-align: center;'>{}</p>"
                "</div>".format(df_year['Name of Company'].nunique()),
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                "<div style='padding: 10px; border-radius: 10px; background-color: #4040FF; "
                "height: 150px;'>"
                "<h3 style='text-align: center;'>Highest CTC</h3>"
                "<p style='text-align: center;'>{}</p>"
                "</div>".format(df_year['CTC'].max()),
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                "<div style='padding: 10px; border-radius: 10px; background-color: #4040FF;"
                "height: 150px;'>"
                "<h3 style='text-align: center;'>Total Offers</h3>"
                "<p style='text-align: center;'>{}</p>"
                "</div>".format(df_year['No. Of Offers'].sum()),
                unsafe_allow_html=True
            )

        with col4:
            st.markdown(
                "<div style='padding: 10px; border-radius: 10px; background-color: #4040FF;"
                "height: 150px;'>"
                "<h3 style='text-align: center;'>Average CTC</h3>"
                "<p style='text-align: center;'>{}</p>"
                "</div>".format(round(df_year['CTC'].mean(), 2)),
                unsafe_allow_html=True
            )
        st.subheader('Top 10 Recruiters (Pie Chart)')
        top_10_companies = df_year.sort_values(by='No. Of Offers', ascending=False).head(10)
        fig = px.pie(top_10_companies, names='Name of Company', values='No. Of Offers', title='Top 10 Recruiters')
        st.plotly_chart(fig)
        
if __name__ == "__main__":
    main()
