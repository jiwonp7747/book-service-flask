from flask import Flask, request, jsonify
import boto3, json
from gemini_api import generate_content
from werkzeug.utils import secure_filename
from socket import *

app = Flask(__name__)

# !! 주의 route 뒤에 경로는 위에 Spring에서 적은 경로와 같아야함 !!
@app.route('/receive_string', methods=['POST'])
def receive_string():
	#Spring으로부터 JSON 객체를 전달받음
    dto_json = request.get_json()
    book_name=dto_json.get('bookName', None)
    
    content =""
    # nickname이 존재하면 generate_content 호출 
    if book_name:
        content = generate_content(book_name)
    else:
        content="닉네임이 존재하지 않습니다."
    
    response_data={"bookName":book_name, "content":content}
    
    # jsonify(response_data)
    print(response_data)
    
    return json.dumps(response_data, ensure_ascii=False)

# 0.0.0.0 으로 모든 IP에 대한 연결을 허용해놓고 포트는 8082로 설정
if __name__ == '__main__':
    app.run('0.0.0.0', port=8082, debug=True)
    
    