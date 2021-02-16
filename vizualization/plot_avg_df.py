#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

import os, re, pprint
import pandas as pd

import pprint

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from players import secondgen_str_text_a as strategy_text

dev_t = 40
tourtype = "second_w_alt"

avrg_win_dict = {}
avrg_norm_dict = {}

x = np.arange(len(strategy_text))

avrg_win_df = pd.DataFrame(index=strategy_text, columns=strategy_text)
avrg_norm_df = pd.DataFrame(index=strategy_text, columns=strategy_text)
avrg_win_df = pd.read_csv("../monteCarlo_tour/results_{}/single_results_1000_200_dev{}/winners_m1000_t200_dev{}.csv".format(tourtype, dev_t, dev_t), index_col=0, converters={'column_name': eval})
avrg_norm_df = pd.read_csv("../monteCarlo_tour/results_{}/single_results_1000_200_dev{}/normed_m1000_t200_dev{}.csv".format(tourtype, dev_t, dev_t), index_col=0, converters={'column_name': eval})

def dict_per_strategy():
    """
    Transform dataframes into dicts for easier manipulation and plotting.
    """
    for strategy in strategy_text:
        temp_list = []
        ###### avrg_norm_df
        for i, row in avrg_norm_df.iterrows():
            list_row = re.split(', ', row[strategy].strip(']['))
            for el in  list_row:
                el = float(el)
            temp_list.append(list_row)
        avrg_norm_dict[strategy] = temp_list
        temp_list = []
        pprint.pprint(strategy)
        #pprint.pprint(avrg_norm_dict[strategy])
        ####### avrg_win_df
        for i, row in avrg_win_df.iterrows():
            list_row = re.split(', ', row[strategy].strip(']['))
            for el in  list_row:
                el = float(el)
            temp_list.append(list_row)
        avrg_win_dict[strategy] = temp_list

def pie_plot(data, strategy):
    # Check if colors where provided, otherwhise use the default color cycle
    path = "{}_dev_run_{}/{}.jpeg".format(tourtype, dev_t, strategy)
    labels = 'P2W', 'P1W', 'EQs'
    explode = (0.1, 0.2, 0.3)
    # second tour pies for 24 strategies
    #fig = plt.figure(figsize=(20,10))
    # first tour pies for 24 strategies
    fig = plt.figure(figsize=(20,10))

    plot_index = 1
    list_index = 0

    while list_index < len(strategy_text):

        ax1 = plt.subplot(4, 6, plot_index)
        
        #ax1 = plt.subplot(6, 4, plot_index)
        plt.xlabel("P2:{}".format(strategy_text[list_index]))
        ax1.pie(data[list_index], explode=explode, autopct='%1.1f%%', shadow=True, startangle=90, radius=3)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plot_index+=1
        list_index+=1

    fig.text(0.06, 0.5, 'P1:{}'.format(strategy),fontsize=15, ha='center', va='center', rotation='vertical')
    plt.legend(labels=labels, loc='upper left')
    plt.tight_layout()
    plt.savefig(path, format='jpeg')
    plt.close('all')


def main():
            
    if not os.path.exists('{}_dev_run_{}/'.format(tourtype, dev_t)):
        print("Creating directory for results.")
        os.makedirs('{}_dev_run_{}/'.format(tourtype, dev_t))
    dict_per_strategy()
    for strategy in strategy_text: 
        pie_plot(avrg_norm_dict[strategy], strategy)
    
    #pprint.pprint(avrg_win_dict)
    #pprint.pprint(avrg_norm_dict)

if __name__ == '__main__':
    main()
