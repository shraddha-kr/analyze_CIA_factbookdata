import streamlit as st
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


image = Image.open('cia.png')

def main():
    # Title
    st.title('Analyze CIA FactBook Data')
    st.image(image, caption='CIA', use_column_width=True)

    # Dropdown menu to select a dataset
    st.write("### Select a Dataset from below: ")
    selected_dataset = select_dataset_file()
    df = pd.read_csv(selected_dataset)

    # Display the dataset
    if st.checkbox("Show Dataset"):
        st.write("### Enter the number of rows to view")
        rows = st.number_input("", min_value=0,value=5)
        if rows > 0:
            st.dataframe(df.head(rows))

    # Select columns to display
    if st.checkbox("Show dataset with selected columns"):
        # get the list of columns
        columns = df.columns.tolist()
        st.write("#### Select the columns to display:")
        selected_cols = st.multiselect("", columns)
        if len(selected_cols) > 0:
            selected_df = df[selected_cols]
            st.dataframe(selected_df)

    # Show the dimension of the dataframe
    if st.checkbox("Show number of rows and columns"):
        st.write(f'Rows: {df.shape[0]}')
        st.write(f'Columns: {df.shape[1]}')

    # Show dataset description
    if st.checkbox("Show description of dataset"):
        st.write(df.describe())

    # Show population countrywise bar-chart
    st.subheader('Top 10 countries by Popuation')

    cols = ['name', 'population']
    df_filtered = df[cols].sort_values(by='population', ascending=False)
    data_to_plot = df_filtered[1:11]


    area_data = pd.DataFrame({
    'index': data_to_plot['name'],
    'population': data_to_plot['population'],
    }).set_index('index')

    st.write(area_data)
    st.bar_chart(area_data)

    # Plot on a world map top ten countries land area wise
    st.subheader('Most Populated Countries')
    latitude = [35.86, 37.09, 56.13, -14.23, -25.27, 20.59, -38.41, 48.01, 28.03, -4.03]
    longitude = [104.19, -95.71, -106.34, -51.92, 133.77, 78.96, -63.61, 66.92, 1.65, 21.75]
    data_to_plot.insert(2, 'latitude', latitude, allow_duplicates = False)
    data_to_plot.insert(3, 'longitude',longitude, allow_duplicates = False)

    st.map(data_to_plot)

    # Show land area countrywise bar-chart
    st.subheader('Top 10 countries by Land Area')

    cols = ['name', 'area_land']
    df_filtered = df[cols].sort_values(by='area_land', ascending=False)
    data_to_plot = df_filtered[1:11]


    area_data = pd.DataFrame({
    'index': data_to_plot['name'],
    'area_land': data_to_plot['area_land'],
    }).set_index('index')

    st.write(area_data)
    st.bar_chart(area_data)


def select_dataset_file():
    dataset_dir = 'datasets'
    filenames = os.listdir(dataset_dir)
    # dropdown menu displaying all the files in dataset directory
    selected_dataset = st.selectbox("",filenames)
    return os.path.join(dataset_dir, selected_dataset)

if __name__ == '__main__':
    main()
