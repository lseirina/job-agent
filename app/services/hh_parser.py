import requests
import time
import json
from urllib.parse import urlencode
import logging


logger = logging.grtLogger(__name__)


class HHparser:
    def __init__(self):
        self.base_url = "https://api.hh.ru"
        self.session = requests.Session()
        
        self.session.headers.update(
            {'User-Agent': 'HH-Agent/1.0 (lseirina87@gmail.com)'}
        )
        
    def search_vacancies(self, skills, experience=None, area = 1):
        """Finding vacancies by keywords and skills."""
        query = " OR ".join(skills + keywords)
        params = {
            'text': query,
            'area': area,
            'per_page': 50,
            'page': 0
        }
        if experience:
            params[experience] = experience
            
        vacancies = []
        
        try:
            response = self.session.get(f"{sel.base_url}/vacancies", params=params)
            response.raise_for_status()
            data = response.json()
            vacancies = data.get('items', [])
            vacancies = vacancies[:20]
            
            logger.info(f"Found {len(vacancies)} vacancies")
        except requests.RequestException as e:
            logger.error(f"Error fetching vacancies: {e}")
            
        return vacancies
            

