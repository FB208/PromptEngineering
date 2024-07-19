from openai import OpenAI

client = OpenAI()

def translate_text(text, target_language):
    # 构建翻译的提示
    prompt = f"Translate the following text to {target_language}: {text}"

    # 调用 OpenAI 接口
    completion = client.chat.completions.create(
    model="gpt-4o-mini-2024-07-18",
    messages=[
        {"role": "user", "content": prompt}
    ]
    )

    # 提取并返回翻译结果
    translated_text = completion.choices[0].message.content.strip()
    return translated_text

