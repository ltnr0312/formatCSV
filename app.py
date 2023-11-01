# Databricks notebook source
import pandas as pd
import numpy as np
import streamlit as st

class Conversor:
    def __init__(self, file):
        self.file = file

    # def preprocess_csv(self):
    #     with open(self.file, 'rb') as csv_file:
    #         result = chardet.detect(csv_file.read())

        names = np.arange(0, 16)
        df = pd.read_csv(self.file, header=6, encoding="iso-8859-1", names=names)
        mylist = df.iloc[-1:].values.tolist().pop(0)
        df.columns = [str(i) for i in mylist]
        df = df.iloc[:-1]
        df = df.iloc[::, :-2]
        df.columns = df.columns.map(lambda x: str(x))
        df = df.astype(float)
        df.iloc[-2, 1:] = df.iloc[-2, :-1].values
        df.iloc[-2, 0] = 0
        index = df.index.tolist()
        index.pop()
        df = df[1:]
        df.reset_index(drop=True, inplace=True)
        df.index = index
        self.df = df

    def get_dataframe(self):
        return self.df

    def save_converted(self, output_format, output_filename):
        if output_format == "csv":
            self.df.to_csv(output_filename, index=True)
        elif output_format == "excel":
            self.df.to_excel(output_filename, index=True)
        else:
            raise ValueError("Invalid output_format. Valid options are 'csv' or 'excel'.")


def main():
    st.title("CSV Conversor")

    file = st.file_uploader("Upload your CSV file")

    if file:
        conversor = Conversor(file)
        conversor.preprocess_csv()

        st.dataframe(conversor.get_dataframe())

        output_format = st.selectbox("Select output format", ("csv", "excel"))

        if st.button("Download"):
            conversor.save_converted(output_format, f"output.{output_format}")

if __name__ == "__main__":
    main()