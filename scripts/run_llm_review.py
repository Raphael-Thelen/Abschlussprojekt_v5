import google.generativeai as genai
import os
import sys
import time

# Load API keys from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Set Prompt for the model
LLM_PROMPT_FILE = "prompt1.txt"

# Ensure API keys are available
if not GEMINI_API_KEY:
    print("Error: Missing API keys. Make sure to set GEMINI_API_KEY.")
    sys.exit(1)
    
genai.configure(api_key=GEMINI_API_KEY)

def read_file_content(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def read_prompt():
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the script
    prompt_file = os.path.join(script_dir, LLM_PROMPT_FILE)  # Construct the absolute path
    
    if not os.path.exists(prompt_file):
        print(f"Error: Prompt file '{prompt_file}' not found.")
        sys.exit(1)
    return read_file_content(prompt_file)

def review_with_gemini(code):
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = read_prompt()
    response = model.generate_content(f"{prompt}\n\n{code}")

    time.sleep(2)  # Wartezeit zwischen Anfragen
    return response.text

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_llm_review.py <file1.py> <file2.py> ...")
        sys.exit(1)
    
    files = sys.argv[1:]
    gemini_results = []
    
    for file in files:
        print(f"Reviewing {file}...")
        code_content = read_file_content(file)
        gemini_results.append(f"### {file}\n" + review_with_gemini(code_content))
    
    with open("llm_review_gemini.txt", "w", encoding="utf-8") as f:
        f.write("\n\n".join(gemini_results))

if __name__ == "__main__":
    main()


