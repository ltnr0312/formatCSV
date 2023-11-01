# Databricks notebook source
import pandas as pd
import numpy as np
import streamlit as st

class Conversor:

    def __init__(self, file):
        self.file = file

    def preprocess_csv(self):
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


def main():
    st.title("Formartar arquivo de CSV")

    file = st.file_uploader("Carregue o seu arquivo CSV")

    if file:
        conversor = Conversor(file)
        conversor.preprocess_csv()

        d = conversor.get_dataframe()

        st.dataframe(conversor.get_dataframe())       

        st.download_button("Façar o download do arquivo no formato csv",
                            d.to_csv(),
                            file_name="csv_converted.csv",
                            mime="text/csv")

if __name__ == "__main__":
    main()