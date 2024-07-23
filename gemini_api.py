import google.generativeai as genai

GOOGLE_API_KEY = 'AIzaSyDRCu-IKmQRRX4WQ3Cmhzkl2oRyP0vO_I0'

genai.configure(api_key=GOOGLE_API_KEY)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

model = genai.GenerativeModel('gemini-pro',
                             generation_config=generation_config)

prompt = """
- 백엔드 개발 관련 책을 5권 추천해주고
- 각 책의 저자와 간단한 설명을 추가해주세요.

"""   

response = model.generate_content(prompt)
print(response.text)