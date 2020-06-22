import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def line_plot(df):
    df.plot(kind = 'line')
    plt.title('Imigrantion from haiti')
    plt.ylabel('Number of imigrant')
    plt.xlabel('Years')
    plt.show()
def plot_area(df):
    df.plot(kind = 'area')
    plt.show()
def hist_plot(df):
    count,bin_edges = np.histogram(df)
    df.plot(kind = 'hist',xticks = bin_edges)
    plt.show()
def bar_plot(df_can):
    df_can = df_can.set_index(["Country"])
    print(df_can.head())
    df_iceland = df_can.loc["Iceland",years]
    df_iceland.plot(kind = 'bar')
    plt.show()
def bar_chart_plot(df):
    df = df.set_index(["Country"])
    
    df_continent = df.groupby('Continent', axis = 0).sum()
    df_continent["Total"].plot(kind = 'pie')
    plt.show()

if __name__  == '__main__':


    path = "D:\IBM Certification\dataVisualization\Canada.xlsx"

    data  = pd.read_excel(path,sheet_name='Canada by Citizenship',
                        skiprows=range(20),
                        skipfooter=2)

    data.columns.tolist()
    data.index.tolist()


    data.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
    years = list(map(int,range(1980,2014)))

    data.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
    column_m = years
    column_m.append("Country")
    #print(column_m)

    df_can = data[column_m]
    #line_plot(df_can)

    df_can["Total"] = df_can.sum(axis = 1)
    #print(df_can.head())
    #print(df_can.isnull().sum())
    #print(df_can.describe())
    data["Total"] = df_can["Total"]
    years.remove("Country")

    df_cannada= df_can.sort_values(['Total'],ascending = False,axis = 0)
    df_top5 = df_cannada.head()

    df_top5 = df_top5[years].transpose()
    #hist_plot(df_can[[2013]])
    ########################################################bar chart#########################################
    #bar_plot(df_can)
    #######################################################################################################
    #bar_chart_plot(data)

