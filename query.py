from prompts import INFERENCE_SYSTEM_PROMPT, INFERENCE_MESSAGES_PROMPT

def query_llm(text: str, client, inference=True):
    system_prompt = INFERENCE_SYSTEM_PROMPT # if inference else
    messages_pronmpt = INFERENCE_MESSAGES_PROMPT # if inference else
    response = client.beta.tools.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=4000,
        temperature=0,
        system=system_prompt,
        messages=[{
            "role": "user",
            "content": f"{messages_pronmpt}{text}"
        }]
    )
    return response.content[0].text # Only works with 1 message