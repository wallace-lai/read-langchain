import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

if __name__ == '__main__':
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(os.path.dirname(curr_dir), ".env")
    _ = load_dotenv(dotenv_path=env_path, override=True)

    # langchain_openai.ChatOpenAI
    gpt_4o = init_chat_model(
        "gpt-4o",
        model_provider="openai",
        temperature=0,
        api_key=os.environ['OPENAI_API_KEY'],
        base_url=os.environ['OPENAI_API_BASE']
    )

    # langchain_deepseek.chat_models.ChatDeepSeek
    deepseek_r1 = init_chat_model(
        "deepseek-r1",
        model_provider="deepseek",
        temperature=0,
        api_key=os.environ['OPENAI_API_KEY'],
        base_url=os.environ['OPENAI_API_BASE']
    )

    # langchain_anthropic.ChatAnthropic
    # claude_opus = init_chat_model(
    #     "claude-opus-4-20250514",
    #     model_provider="anthropic",
    #     temperature=0,
    #     api_key=os.environ['OPENAI_API_KEY'],
    #     base_url=os.environ['OPENAI_API_BASE']
    # )

    # langchain_google_vertexai.ChatVertexAI
    # gemini_15 = init_chat_model(
    #     "gemini-2.5-pro",
    #     model_provider="google_genai",
    #     temperature=0,
    #     api_key=os.environ['OPENAI_API_KEY'],
    #     base_url=os.environ['OPENAI_API_BASE']
    # )

    print("GPT-4o: " + gpt_4o.invoke("what's your name").content + '\n')
    print("Deepseek-r1 : " + deepseek_r1.invoke("what's your name").content + '\n')

    # print("Claude Opus: " + claude_opus.invoke("what's your name").content + '\n')
    # print("Gemini 2.5: " + gemini_15.invoke("what's your name").content + '\n')


