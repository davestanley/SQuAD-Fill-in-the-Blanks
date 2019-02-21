# Set up and load data
# Includes
import sys
import os
import numpy as np
import json
import os


# Setup paths containing utility
curr_folder = os.getcwd()
sys.path.insert(0, os.path.join(curr_folder,'modules'))

# Utils imports for loading data
from utils import save_data, load_data, exists_datafolder
from utils import load_SQuAD_train, load_SQuAD_dev
from utils import get_foldername
from utils import merge_artfiles
from utils_EDAplots import plotbar_train_dev,plothist_train_dev

# Path for saving data
foldername_save = '.'            # By default, this will save to data/.

# Load the original data
arts_train = load_SQuAD_train()
arts_dev = load_SQuAD_dev()


# Load blanks data (ground truth) [call this arts3]
foldername = get_foldername('sq_pp_training')
arts3train = load_data('train.json',foldername)
arts3dev = load_data('dev.json',foldername)


# # # # # # Training data # # # # # #
arts = arts_train
arts3 = arts3train

# Make sure all titles match
all_title_pairs = [(a1['title'],a3['title']) for a1,a3 in zip(arts,arts3)]
titles_match_bool = [a1['title'] == a3['title'] for a1,a3 in zip(arts,arts3)]
print("Matching titles: {} \nTotal articles {}".format(sum(titles_match_bool),len(titles_match_bool)))

# Merge ground truth blanks with original data to get full dataset
from utils_SQuAD import merge_arts_paragraph_fields
list_of_fields = ['context_blanked','blank_classification']
arts_merged = merge_arts_paragraph_fields(arts,arts3,list_of_fields)

# Finally, save the data
save_data(arts_merged,'train.json',foldername_save);


# # # # # # Dev data # # # # # #
arts = arts_dev
arts3 = arts3dev

# Make sure all titles match
all_title_pairs = [(a1['title'],a3['title']) for a1,a3 in zip(arts,arts3)]
titles_match_bool = [a1['title'] == a3['title'] for a1,a3 in zip(arts,arts3)]
print("Matching titles: {} \nTotal articles {}".format(sum(titles_match_bool),len(titles_match_bool)))

# Merge ground truth blanks with original data to get full dataset
from utils_SQuAD import merge_arts_paragraph_fields
list_of_fields = ['context_blanked','blank_classification']
arts_merged = merge_arts_paragraph_fields(arts,arts3,list_of_fields)

# Finally, save the data
save_data(arts_merged,'dev.json',foldername_save);
