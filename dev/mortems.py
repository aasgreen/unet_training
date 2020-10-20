import pathlib
import os
import re
import pandas as pd


'''
library dedicated to visualiztion of training progress.
'''

def create_timeline():
    def gen_tree(name):
        result = []
        for root, dirs, files in os.walk(pathlib.Path('./experiments/')):
            if name in files:
                result.append(os.path.join(root,name))
        res_df = pd.DataFrame({'names':result})
        res_df['dates'] = res_df['names'].str.extract('(\d*\-\d*-\d*_\d*-\d*-\d*)')
        res_df['type'] = res_df['names'].str.extract('\d*/([a-z]*)\.')
        res_df['dates'] = pd.to_datetime(res_df['dates'], format= '%Y-%m-%d_%H-%M-%S')
        res_df= res_df.sort_values('dates')

    
        return res_df



    summaries = gen_tree('summary.md')
    logs = gen_tree('log.dat')

    res = pd.concat([summaries,logs])
    res = res.sort_values('dates')
    return res


def print_summary(names_df, output_name):
    '''
    print out summary from files contained within names_df (should have summary and log data)
    args:
        names_df, dataframe[names, dates], containing filenames for both logs and summaries
        output_name: str, path for the summary to be printed in
    '''
    date_gp = names_df.groupby('dates')
    with open(output_name, 'w') as fout:
        for g_name, group in date_gp:
            log_name = group['names'][group['type'] == 'log']
            sum_name = group['names'][group['type'] == 'summary']

            try:
                log = pd.read_csv(log_name.values[0])
                print(log)
            except:
                print('log file not found: {}'.format(g_name))
                print(log_name.values)

            try:
                with open(sum_name.values[0], 'r') as f_in:
                    summary = f_in.read()
                    print(summary)
            except:
                print('summary file not found: {}'.format(g_name))
            #print(sum_name)


res = create_timeline()
test = print_summary(res, './timeline.md')

