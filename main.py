import sys
import os
from reddit_scraper import scrape_user_content
from persona_builder import generate_persona

def extract_username(profile_url):
    return profile_url.strip('/').split('/')[-1]

def save_to_file(username, content):
    os.makedirs("output", exist_ok=True)
    filepath = f"output/{username}_persona.txt"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Persona saved to: {filepath}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <reddit_profile_url>")
        sys.exit(1)

    profile_url = sys.argv[1]
    username = extract_username(profile_url)

    print(f"🔍 Scraping content for: {username}")
    user_content = scrape_user_content(username)

    print("🧠 Generating persona...")
    persona = generate_persona(user_content)

    save_to_file(username, persona)
