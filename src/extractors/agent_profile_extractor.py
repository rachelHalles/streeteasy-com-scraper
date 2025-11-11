thonimport requests
from bs4 import BeautifulSoup

class AgentProfileExtractor:
    def __init__(self):
        self.base_url = "https://streeteasy.com"
    
    def extract_agent_profile(self, property_data):
        agent_url = property_data.get("urlPath")
        if agent_url:
            response = requests.get(agent_url)
            soup = BeautifulSoup(response.content, "html.parser")
            agent_profile = self.parse_agent_profile(soup)
            return agent_profile
        return None

    def parse_agent_profile(self, soup):
        agent_name = soup.find("div", class_="agent-name").text.strip()
        agent_phone = soup.find("div", class_="agent-phone").text.strip() if soup.find("div", class_="agent-phone") else None
        agent_email = soup.find("div", class_="agent-email").text.strip() if soup.find("div", class_="agent-email") else None
        
        agent_profile = {
            "name": agent_name,
            "phone": agent_phone,
            "email": agent_email
        }
        return agent_profile