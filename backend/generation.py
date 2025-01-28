from groq import Groq
import os

groq_key= os.getenv("Groq_API_key")
assert(groq_key != None, "Groq Key not found")

groq_client= Groq(groq_key)