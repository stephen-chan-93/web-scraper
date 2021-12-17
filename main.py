import numpy as np
import pandas as pd # pandas for dataframe based data

import requests
from bs4 import BeautifulSoup # HTML parsing
import bs4

from fastnumbers import isfloat
from fastnumbers import fast_float
from multiprocessing.dummy import Pool as ThreadPool

import matplotlib.pyplot as plt
import seaborn as sns
import json
from tidylab import tidy_document # html linter

sns.set_style('whitegrid')
from IPython.core.interactiveshell import InteractiveShell 
InteractiveShell.ast_node_interactivity = "all"
