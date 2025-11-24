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
        
    def search_vacancies(self, skills, experience=None):
        """Finding vacancies by keywords and skills."""
        query = " OR ".join(skills + keywords)
        params = {
            'text': query,
            'per_page': 50,
            'page': 0
        }
        if experience:
            params[experience] = experience
            
        vacancies = []
        
        try:
            response = self.session.get(f"{self.base_url}/vacancies", params=params)
            response.raise_for_status()
            data = response.json()
            vacancies = data.get('items', [])
            vacancies = vacancies[:20]
            
            logger.info(f"Found {len(vacancies)} vacancies")
        except requests.RequestException as e:
            logger.error(f"Error fetching vacancies: {e}")
            
        return vacancies
    
    def get_vacancy_detail(self, vacancy_id):
        """Return datails of vacancy."""
        try:
            time.sleep(0.1)
            response = self.session.get(f"{self.base_url}/vacancies/{vacancy_id}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error fetching vacancy {vacancy_id}: {e}")
            return None
        
    def parse_vacancy_data(seelf, vacancy_data):
        """Parse vacancy data into normal format."""
        return {
            'hh_id': str(vacancy_data['id']),
            'name': vacancy_data.get('name', ''),
            'url': vacancy_data.get('alternate_url', '')
            'description': self._clean_description(vacancy_data.get('description', ''))
            'skills': self._extract_skills_from_description(vacancy_data('description', ''))
            'experience': vacancy_data.get('experience', {}).get('name', ''),
            'employment_type': vacancy_data.get('employment', {}).get('name', '')
        }
    
    def _extract_skills_from_description(self, description):
        """Extract skills and turn into normal form."""
        common_skills = [
        'python', 'sql', 'postgresql', 'git', 'linux', 'docker', 
        'docker-compose', 'django', 'flask', 'fastapi', 'aws', 'nginx', 'rest', 
        'api', 'http', 'json', 'alembic', 'sqlalchemy', 'pytest', 'gitlab', 
        'pep8', 'solid', 'backend', 'algorithms', 'design patterns', 'database',
        'web applications', 'asynchronous programming'
    ]
        found_skills = []
        
        for skill in common_skills:
            if skill in description.lower():
                found_skills.append(skill)
                
        return ', '.join(found_skills)
            
            

