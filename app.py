# Databricks notebook source
# AI-Assisted

import pandas as pd
import numpy as np
import chardet

class Conversor:
    def __init__(self, uri):
        self.uri = uri

    def preprocess_csv(self):
        with open(self.uri, 'rb') as csv_file:
            result = chardet.detect(csv_file.read())

        names = np.arange(0, 16)
        df = pd.read_csv(self.uri, header=6, encoding=result['encoding'], names=names)
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