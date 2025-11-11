thonimport json
from extractors.property_parser import PropertyParser
from extractors.agent_profile_extractor import AgentProfileExtractor
from outputs.exporter import Exporter
import os

def run_scraper():
    # Setup paths
    input_file = "data/inputs.sample.txt"
    output_file = "data/sample.json"
    
    # Read input data
    with open(input_file, "r") as file:
        start_urls = file.readlines()
    
    # Process each URL
    property_parser = PropertyParser()
    agent_extractor = AgentProfileExtractor()
    exporter = Exporter()
    
    all_properties = []
    for url in start_urls:
        properties = property_parser.parse_properties(url.strip())
        for property in properties:
            agent_profile = agent_extractor.extract_agent_profile(property)
            property['agent_profile'] = agent_profile
            all_properties.append(property)
    
    # Export data
    exporter.export_to_json(all_properties, output_file)
    print(f"Scraping complete. Data saved to {output_file}")

if __name__ == "__main__":
    run_scraper()