
import pandas as pd

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np


def vaffle_chart(df):
    total_values = sum(df['Total'])
    category_proportions = [(float(value)/total_values) for value in df['Total']]
    for i, proportion in enumerate(category_proportions):
        print (df_dsn.index.values[i] + ': ' + str(proportion))
    #defining overall size of waffle chart
    width = 40
    height = 10
    total_num_tiles = width * height
    print ('Total number of tiles is ', total_num_tiles)
    tiles_per_category = [(proportion * total_num_tiles) for proportion in category_proportions]
    #initialize the waffle chart as an empty matrix
    waffle_chart = np.zeros((height,width))
    category_index = 0
    tile_index = 0
    for col in range(width):
        for row in range(height):
            tile_index += 1
            if tile_index > sum(tiles_per_category[0:category_index]):
                category_index += 1
            
            waffle_chart[row,col] = category_index
    print("waffle chart populated")
    print(waffle_chart)
    fig = plt.figure()
    colormap = plt.cm.coolwarm
    plt.matshow(waffle_chart,cmap = colormap)
    plt.colorbar()
    # get the axis
    ax = plt.gca()

    # set minor ticks
    ax.set_xticks(np.arange(-.5, (width), 1), minor=True)
    ax.set_yticks(np.arange(-.5, (height), 1), minor=True)
        
    # add gridlines based on minor ticks
    ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

    plt.xticks([])
    plt.yticks([])
    # compute cumulative sum of individual categories to match color schemes between chart and legend
    values_cumsum = np.cumsum(df_dsn['Total'])
    total_values = values_cumsum[len(values_cumsum) - 1]

    # create legend
    legend_handles = []
    for i, category in enumerate(df_dsn.index.values):
        label_str = category + ' (' + str(df_dsn['Total'][i]) + ')'
        color_val = colormap(float(values_cumsum[i])/total_values)
        legend_handles.append(mpatches.Patch(color=color_val, label=label_str))

    # add legend to chart
    plt.legend(handles=legend_handles,
            loc='lower center', 
            ncol=len(df_dsn.index.values),
            bbox_to_anchor=(0., -0.2, 0.95, .1)
            )
    plt.show()
if __name__ == '__main__':
    path = "D:\IBM Certification\dataVisualization\Canada.xlsx"
    df_can  = pd.read_excel(path,sheet_name='Canada by Citizenship',
                        skiprows=range(20),
                        skipfooter=2)
    df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis = 1, inplace = True)
    df_can.rename (columns = {'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace = True)
    df_can.columns = list(map(str, df_can.columns))

    df_can.set_index('Country', inplace = True)

    df_can['Total'] =  df_can.sum (axis = 1)

    years = list(map(str, range(1980, 2014)))
    print ('data dimensions:', df_can.shape)
    
    df_dsn = df_can.loc[['Denmark', 'Norway', 'Sweden'], :]
    vaffle_chart(df_dsn)
