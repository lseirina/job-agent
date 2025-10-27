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
        
    def parse_resume(self):
        with open(self.resum_part, 'r', encoding='utf-8') as file:
            content = file.read()
            
        skills_section = self._extract_section(content, ['навыки', 'skills', 'технологии'])
        self.skills = self._extract_skills(skills_section)    
        experience_section = self._extract_section(content, ['опыт', 'experience'])
        self.experience = self._extract_experience(experience_section) 
        
        self.key_words = self._extract_keywords(content)
        
        return { 'skills' : self.skills,
                'experience': self.experience,
                'keywords': self.keywords,
                'raw_text': content
            }
        
    def _extract_section(self, content, section_names):
        content_lower = content.lower()
        for name in section_names:
            pattern = rf'{name}[\s\S]*?(?=\n\s*\n|$)'
            match = re.search(pattern, content_lower, re.IGNORECASE)
            if match:
                return match.group()
        return ""