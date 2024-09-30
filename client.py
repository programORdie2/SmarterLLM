from groq import Groq
from vars import GROQ_API_KEY, SYSTEM_PROMPT

# Initialize the Groq client
client = Groq(api_key=GROQ_API_KEY)