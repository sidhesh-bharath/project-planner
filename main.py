from google import genai
import os
from rich.console import Console
from rich.markdown import Markdown
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

client = genai.Client(api_key=API_KEY)

def export_file(filename, content):
    if os.path.exists(f"{os.getcwd()}/saved-projects/") is False:
        os.mkdir(f"{os.getcwd()}/saved-projects/")
    with open(f"{os.getcwd()}/saved-projects/{filename}", "w") as file:   
        file.write(content)

def parse_idea(idea, length, project_duration):
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"You are a project mentor. You will help me plan my project tasks effectively. This is my project description: '{idea}' and I have decided to allocate around {project_duration} weeks for it. Please provide a task breakdown and timeline alongwith a checklist for me to follow in a clean and structured format and make it {length} stick to it being {length}.",
)   
    file_name = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"Convert the following project idea into a suitable file name by removing spaces and special characters: '{idea}'. Max 3 words, all lowercase, and add .txt at the end while separating the words by using a hyphen. ONLY provide the file name as output without any extra text.",
)
    return response, file_name

def get_user_input():
    idea = input("Enter your project idea: ")
    length = input("Desired length of the plan (short/medium/long): ").strip().lower()
    project_duration = input("Estimated project duration (in weeks): ").strip()
    export = input("Do you want to export the plan to a file? (yes/no): ").strip().lower()

    print("AI is generating your project plan, please wait...")

    response, filename = parse_idea(idea, length, project_duration)
    os.system("cls" if os.name == "nt" else "clear")

    console = Console()
    clean_response = Markdown(response.text)

    console.print(clean_response)

    if export == "yes":
        export_file(filename.text, response.text)
        print(f"""
✅Project plan exported to /saved-projects/{filename.text}\n
""")

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    get_user_input()