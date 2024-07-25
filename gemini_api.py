import google.generativeai as genai
from api_key import GOOGLE_API_KEY

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

# prompt = """
# - 백엔드 개발 관련 책을 5권 추천해주고
# - 각 책의 저자와 간단한 설명을 추가해주세요.

# """   

def generate_content(book):
  
    prompt = f"""
    - {book} 책에 대해서 설명해주세요.
    - 단 50자 안으로 설명해주세요.
    """   
    generate_content_response = model.generate_content(prompt)
    content=generate_content_response.text
    
    return content
  
  
