import os
from typing import List
from pydantic import BaseModel, Field
from pydantic_ai import Agent
# from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.ollama import OllamaProvider

provider = OllamaProvider(
    base_url='http://localhost:11434/v1'
)

# 1. Define the Data Model
class CodeResponse(BaseModel):
    language: str = Field(description="The programming language used in the code.")
    code: str = Field(description="The generated code snippet.")
    explanation: str = Field(description="A brief explanation of how the code works.")
    optimization_tips: List[str] = Field(description="A list of tips to optimize or improve the code.")

# 2. Configure the Model (Ollama acts as an OpenAI-compatible endpoint)
# We use a dummy API key because Ollama doesn't require one, but the client expects it.
model = OpenAIChatModel(
    'deepseek-coder-v2:lite',
    provider=provider
)

# 3. Initialize the Agent
coder_agent = Agent(
    model,
    output_type=CodeResponse,
    system_prompt=(
        "You are a local coding assistant specialized in providing structured, type-safe code snippets. "
        "Always return the response in the requested JSON structure. "
        "Provide clear explanations and practical optimization tips."
    ),
)