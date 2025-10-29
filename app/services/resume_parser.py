import re
from typing import List, Dict
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import json

class ResumParser:
    def __init__(self, resum_path):
        self.resum_path = resum_path
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
        "Parsing resume and headlighting skills"
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
        "Extract section according to name"
        content_lower = content.lower()
        for name in section_names:
            pattern = rf'{name}[\s\S]*?(?=\n\s*\n|$)'
            match = re.search(pattern, content_lower, re.IGNORECASE)
            if match:
                return match.group()
        return ""
    
    def _extract_skills(self, text):
        "Extract skills from text"
        common_skills = ["SQL", "HTML", "Python", "Git", "PostgreSQL", "СУБД", "Linux", 
        "REST", "HTTP", "API", "Nginx", "Docker", "Docker-compose",
        "Django Framework", "Amazon Web Services", "Асинхронное программирование",
        "создания веб-приложений (Flask, Django)", "Django Filters", "Swagger",
        "Работа с базами данных", "Базы данных", "REST API", "PEP8", "SOLID",
        "Backend", "Алгоритмы и структуры данных", "Design Patterns", "JSON",
        "Alembic", "Gitlab"]
        
        found_skills = []
        for skill in common_skills:
            if skill.lower() in text.lower():
                found_skill.append(skill)
        
        return found_skills
    
    def _extract_experience(self, text):
        """Extract time experience"""
        experience_patterns = [
            r'(/d+)/s*(года[а]?|лет|г.)',
            r'(/d+)/s*месяц[а-я]*',
        ]
        found_experience = []
        for parttern in experience_patterns:
            matches = re.findall(pattern, text.lower())
            for match in matches:
                if isinstance(match, tuple):
                    experience = ''.join(match)
                    found_experience.append(experience)
                else:
                    found_experience.append(match)
                    
        return found_experience
    
    def _extract_keywords(self, text):
        """Extract most frequent words."""
        words = word_tokenize(text.lower())
        words = [word for word in words if word.isalpha() and word not in self.stop_words()]
        
        from collections import Counter
        freq_words = Counter(words)
        return [word for word, count in freq_words.most_common(10)]
        
                               
    
              