import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def dataClean(dataframe):
    for i in boxPlotcols:
        if i != 'age':
            q1 = dataframe[i].quantile(0.25)
            q3 = dataframe[i].quantile(0.75)

            iqr = q3 - q1

            lf = q1 - 1.5 * iqr
            uf = q3 + 1.5 * iqr

            dataframe[i] = dataframe[i][(dataframe[i] >= lf) & (dataframe[i] <= uf)] 

    return dataframe

def nullCol(dataframe):
    for i in dataframe.columns:
        if dataframe[i].isna().sum() > 1:
            dataframe[i] = dataframe[i].fillna(method = 'bfill')
        else:
            pass

    return dataframe

def heartDisease(dataframe):
    hy = (dataframe.iloc[:,-1].value_counts()[1] / dataframe.iloc[:,-1].count())
    hn = (dataframe.iloc[:,-1].value_counts()[0] / dataframe.iloc[:,-1].count()) 
    output = (f"{hn * 100: .2f}% patients i.e., {dataframe.iloc[:,-1].value_counts()[0]} do not have heart diseases\n"
              f"{hy * 100: .2f}% patients i.e., {dataframe.iloc[:,-1].value_counts()[1]} have heart diseases")
    return output

boxPlotcols = ['age','trestbps','chol','thalach','oldpeak']

@st.cache_data # Instead of loading data repeatedly while we are caching data
def load_data():
    df = pd.read_csv('heart.xls', sep = '\t')
    df.rename(columns = {"target":"heart_disease"}, inplace  = True)
    df = dataClean(df)
    df = nullCol(df)

    return df

df = load_data()

def show_explore_page():

    st.title("Explore Heart Disease prediction dataset")

    st.write("#### The following data analysis is with respect to UCI Heart Dataset")

    fig1, ax1 = plt.subplots(figsize = (5,5))
    ax1.pie(x = df.heart_disease.value_counts(), startangle=90, 
        autopct = lambda p:f'{p:.2f}%, \n {p*sum(df.heart_disease.value_counts().values)/100 :.0f} Patients', 
        frame = False, labels = ['Heart disease', 'No heart disease'])
    plt.title('Patients with and with out heart diseases', fontweight = 'bold')

    st.pyplot(fig1)

    fig2, ax2 = plt.subplots(figsize = (5,5))
    ax2.pie(x = df.sex.value_counts(), startangle=90, 
        autopct = lambda p:f'{p:.2f}%, \n {p*sum(df.heart_disease.value_counts().values)/100 :.0f} Patients', 
        frame = False, labels = ['Male', 'Female'])
    plt.title('Gender wise Patients', fontweight = 'bold')

    st.pyplot(fig2)

    fig3, ax3 = plt.subplots()
    ax3 = sns.histplot(x = df.age[df.heart_disease == 0], kde = True, edgecolor = 'black', color = 'blue')
    ax3.lines[0].set_color('green')
    plt.xlabel('Age', fontweight = 'bold')
    plt.ylabel('Number of People', fontweight = 'bold')
    plt.title('Age with respect to No heart disease', fontweight = 'bold')
    ax3.bar_label(ax3.containers[0], fontsize = 8)

    st.pyplot(fig3)

    fig4, ax4 = plt.subplots()
    ax4 = sns.histplot(x = df.age[df.heart_disease == 1], kde = True, edgecolor = 'black', color = 'orange')
    ax4.lines[0].set_color('red')
    plt.xlabel('Age', fontweight = 'bold')
    plt.ylabel('Number of People', fontweight = 'bold')
    plt.title('Age with respect to heart disease', fontweight = 'bold')
    ax4.bar_label(ax4.containers[0], fontsize = 8)

    st.pyplot(fig4)
