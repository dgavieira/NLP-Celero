from read_test import *
from read_train import *

path_test_pos = str(input('Insert test path for positive data'))
path_test_neg = str(input('Insert test path for negative data'))

path_train_pos = str(input('Insert train path for positive data'))
path_train_neg = str(input('Insert train path for negative data'))
path_train_unsup = str(input('Insert train path for unsuposed data'))

# Data Extraction

read_test_pos(path_test_pos)
read_test_neg(path_test_neg)

read_train_pos(path_train_pos)
read_train_neg(path_train_neg)
read_train_unsup(path_train_unsup)
