import os
import openai
openai.organization = "org-4cnk4lHqvRBWiiqFEbVs4X4e"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()