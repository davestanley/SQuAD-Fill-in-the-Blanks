# Set up and load data
# Includes
import sys
import os

# Setup paths containing utility
curr_folder = os.getcwd()
sys.path.insert(0, os.path.join(curr_folder,'modules'))

# Import utils
from utils_EDA import p_list_qas
from utils import load_SQuAD_train
from utils import load_SQuAD_dev
from utils_SQuAD import classify_blanks_from_answers

# Load the training data
arts_train = load_SQuAD_train()

# Load the testing data
arts_dev = load_SQuAD_dev()

# All articles
Ntrain = len(arts_train)
Ndev = len(arts_dev)
print ("Narticles in train = " +  str(len(arts_train)))
print ("Narticles in dev = " +  str(len(arts_dev)))

# Settings
maxWords_per_FITB = 2            # We conly consider answers with at most this many words for blanking out

# # TRAINING DATASET # #
art = arts_train[:]

# Run the classifier
art3 = classify_blanks_from_answers(art,maxWords_per_FITB=2,return_full=False)

# Do a test print
print(art3[0]['title'])
print(art3[0]['paragraphs'][0]['context_blanked'])

# # Save the file
from utils import get_foldername, save_data
foldername = get_foldername('sq_pp_training')
save_data(art3,'train.json',foldername);



# # DEV DATASET # #
art = arts_dev[:]

# Run the classifier
arts3dev = classify_blanks_from_answers(art,maxWords_per_FITB=2,return_full=False)

# Do a test print
print(arts3dev[0]['title'])
print(arts3dev[0]['paragraphs'][0]['context_blanked'])


# # Save the file
from utils import get_foldername, save_data
foldername = get_foldername('sq_pp_training')
save_data(arts3dev,'dev.json',foldername);
