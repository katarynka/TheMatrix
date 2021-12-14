import csv
import numpy as np

relative_path = "experiments/horse_race/horse_race_results/"
column_titles = ["n","time","stdv"]

sleep = False
warm_up = True


n_list = [2,4,8,16]
N = 2
s = 4 ## to be changed!!!! s256
m_strassen = 4 # change!!!! m8
m_write_trhough = 4 # change1!!! m256

def write_csv(n_list: list, res: np.ndarray, filename: str, column_titles:str=None):
    """write_csv

    Args:
        n_list (list): list of n (the matrix side length) that the the experiment is run with
        res (np.ndarray): results from the experiment
        filename (str): the filename that you desire
        column_titles (lst): takes a list with the columns title for the csv file. The titles should be given comma seperated words and no spaces
    """
    with open(filename ,'w') as f:
        writer = csv.writer(f)
        if column_titles != None:
            writer.writerow(column_titles)
        for i in range(len(n_list)):
            writer.writerow ([n_list[i]] + res[i,:].tolist())