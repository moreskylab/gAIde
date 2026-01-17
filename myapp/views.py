from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .agent import coder_agent


async def chat_view(request: HttpRequest) -> HttpResponse:
    context = {}

    if request.method == "POST":
        user_prompt = request.POST.get("prompt")

        if user_prompt:
            try:
                # Run the agent asynchronously
                # PydanticAI handles the validation internally
                result = await coder_agent.run(user_prompt)

                # result.data is an instance of the CodeResponse Pydantic model
                context['response'] = result.data
                context['user_prompt'] = user_prompt

            except Exception as e:
                # Handle connection errors (e.g., Ollama not running) or validation errors
                context['error'] = f"Error processing request: {str(e)}"

    return render(request, "chat.html", context)