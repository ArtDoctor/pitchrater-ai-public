import requests
import openai


gpt_api_key = ''
openai.api_key = gpt_api_key


def send_text_to_chatgpt(slides_text: str, debug=True) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Provide feedback for the following pitch deck slides text. Note that any missing or erroneous words or symbols may be due to the OCR process, don't mention them in your feedback and don't take them into account. Here is extracted text, without any images and visuals: " + slides_text
            }
        ]
    )
    if debug:
        print("Got feedback from GPT successfully")
    return response['choices'][0]['message']['content']
