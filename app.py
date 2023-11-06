# Databricks notebook source
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO

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

    def format_cells_with_colors(self):
        df = self.df
        num_rows, num_columns = df.shape
        color_df = pd.DataFrame("", index=df.index, columns=df.columns)

        for i in range(num_rows):
            while i < 10:
                for j in range(3):
                    color_df.iloc[i,j] = "red" 
                break

            while i < 8:
                color_df.iloc[i, 3] = "red"
                break

            while i < 6:
                color_df.iloc[i, 4] = "red"
                break

            while i < 5:
                color_df.iloc[i, 5] = "red"
                break

            while i < 4:
                color_df.iloc[i, 6] = "red"
                break

            while i < 3:
                color_df.iloc[i, 7] = "red"
                break

            while i < 2:
                for k in np.arange(8,num_columns):
                    color_df.iloc[i, k] = "red"
                break

            while i == 10:
                for l in range(4):
                    color_df.iloc[i,l] = "yellow" 
                break

            while i > 7 and i < 10:
                for m in np.arange(3, 5):
                    color_df.iloc[i,m] = "yellow"
                break

            while i > 5 and i < 9:
                for n in np.arange(4, 6):
                    color_df.iloc[i,n] = "yellow"
                break

            while i > 4 and i < 7:
                for n in np.arange(5, 7):
                    color_df.iloc[i,n] = "yellow"
                break

            while i > 3 and i < 6:
                for n in np.arange(6, 8):
                    color_df.iloc[i,n] = "yellow"
                break

            while i > 2 and i < 5:
                for n in np.arange(7, 10):
                    color_df.iloc[i,n] = "yellow"
                break

            while i > 1 and i < 4:
                for n in np.arange(8, 11):
                    color_df.iloc[i,n] = "yellow"
                break

            while i == 2:
                color_df.iloc[i, 11] = "yellow"
                break

            while i > 10:
                for n in np.arange(0, 5):
                    color_df.iloc[i,n] = "green"
                break

            while i > 9 and i < 13:
                for n in np.arange(4, 6):
                    color_df.iloc[i,n] = "green"
                break

            while i > 8 and i < 12:
                for n in np.arange(5, 7):
                    color_df.iloc[i,n] = "green"
                break

            while i > 6 and i < 11:
                for n in np.arange(6, 8):
                    color_df.iloc[i,n] = "green"
                break

            while i > 5 and i < 10:
                for n in np.arange(7, 9):
                    color_df.iloc[i,n] = "green"
                break

            while i > 4 and i < 9:
                for n in np.arange(8, 10):
                    color_df.iloc[i,n] = "green"
                break

            while i > 3 and i < 8:
                color_df.iloc[i, 10] = "green"
                break

            while i > 2 and i < 7:
                color_df.iloc[i, 11] = "green"
                break

            while i > 1 and i < 6:
                color_df.iloc[i, 12] = "green"
                break

            while i > 1 and i < 5:
                color_df.iloc[i, 13] = "green"
                break

            while i == 13:
                for n in np.arange(5, num_columns):
                    color_df.iloc[i,n] = "#D2691E" 
                break

            while i == 12:
                for n in np.arange(6, num_columns):
                    color_df.iloc[i,n] = "#D2691E"
                break

            while i == 11:
                for n in np.arange(7, num_columns):
                    color_df.iloc[i,n] = "#D2691E"
                break

            while i == 10:
                for n in np.arange(8, num_columns):
                    color_df.iloc[i,n] = "#D2691E"
                break

            while i == 9:
                for n in np.arange(9, num_columns):
                    color_df.iloc[i,n] = "#D2691E"
                break

            while i == 8:
                for n in np.arange(10, num_columns):
                    color_df.iloc[i,n] = "#D2691E"
                break

            while i == 7:
                for n in np.arange(11, num_columns):
                    color_df.iloc[i,n] = "#D2691E"
                break

            while i == 6:
                for n in np.arange(12, num_columns):
                    color_df.iloc[i,n] = "#D2691E"
                break

            while i == 5:
                color_df.iloc[i, 13] = "#D2691E"
                break

            self.color_df = color_df

        def apply_colors(_):
            styled_df = pd.DataFrame('', index=df.index, columns=df.columns)
            for row in range(color_df.shape[0]):
                for col in range(color_df.shape[1]):
                    bg_color = color_df.iat[row, col]
                    text_color = color_map.get(bg_color, 'black')  # Default text color is black if not found in the color_map
                    styled_df.iat[row, col] = f"background-color: {bg_color}; color: {text_color};"
            return styled_df

        color_map = {
                        'red': 'white',
                        '#D2691E': 'white',
                        'green': 'white',
                        'yellow': 'black',
                        # Add more color mappings as needed
        }

        formatted_df = df.style.apply(apply_colors, axis=None)
        self.formatted_df = formatted_df

    def get_formatted_dataframe(self):
        return self.formatted_df
    
    def get_color_counts(self):
        color_counts = self.color_df.stack().value_counts()
        grouped_counts = color_counts.groupby(color_counts.index).sum().sort_values(ascending=False)        
        return grouped_counts

    def get_color_counts_renamed(self):
        color_counts = self.color_df.stack().value_counts()
        grouped_counts = color_counts.groupby(color_counts.index).sum().sort_values(ascending=False)
        colors, counts = zip(*color_counts.items())
        color_names = {
                        'red': 'Carga Crítica',
                        'green': 'Operação Adequada',
                        '#D2691E': 'Alto RPM x Baixa Carga',
                        'yellow': 'Carga Excessiva'
                    }
        updated_labels = [color_names[color] for color in colors]
        grouped_counts.index = updated_labels         
        return grouped_counts

def create_bar_graph(color_counts):

    # Update color names using the requested dictionary
    color_names = {
        'red': 'Carga Crítica',
        'green': 'Operação Adequada',
        '#D2691E': 'Alto RPM x Baixa Carga',
        'yellow': 'Carga Excessiva'
    }

    fig, ax = plt.subplots()

    colors, counts = zip(*color_counts.items())

    ax.bar(colors, counts, color=colors)
    ax.bar_label(ax.containers[0])
    ax.set_xlabel("Regime de Operação", labelpad=20)
    ax.set_ylabel("Quantidade de Operações")
    ax.set_title("Regimes de Operação x Quantidade", pad=20)


    # Create a list of updated_labels using color_names dictionary
    updated_labels = [color_names[color] for color in colors]

    # Set x-axis labels rotation to 45 degrees
    ax.set_xticklabels(updated_labels, rotation=45)

    # Adjust the plot layout
    fig.tight_layout()

    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=100)
    buf.seek(0)
    return buf

def main():
    st.title("Formatar arquivo de CSV")

    file = st.file_uploader("Carregue o seu arquivo CSV")

    if file:
        conversor = Conversor(file)
        conversor.preprocess_csv()
        conversor.format_cells_with_colors()

        d = conversor.get_dataframe()

        st.write(conversor.get_formatted_dataframe())

        color_counts = conversor.get_color_counts()
        color_counts_renamed = conversor.get_color_counts_renamed()

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Tabela")
            st.dataframe(color_counts_renamed)

        with col2:
            st.subheader("Gráfico")
            graph_buf = create_bar_graph(color_counts)
            st.image(graph_buf, caption="Regime de Operação x Quantidade", use_column_width=True, output_format='PNG')


        st.download_button("Faça o download do arquivo no formato csv",
                            d.to_csv(),
                            file_name="csv_converted.csv",
                            mime="text/csv")

if __name__ == "__main__":
    main()