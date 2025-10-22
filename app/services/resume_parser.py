import re
from typing import List, Dict
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import json

class ResumParser:
    def __init__(self, resum_path):
        self.tresum_path = resum_path
        self.skills = []
        self.experience = []
        self.keywords = []
        
        try:
            nltk.data.find('tokenizers/punkt')
        except LookUpError:
            nltk.download(punkt)
        try:
            nltk.data.find('corpora/stopwords')
        except LookUpError:
            nltk.download('stopwords')
            
        self.stop_words = set(stopwords.words('russian') + stopwords.words('english'))