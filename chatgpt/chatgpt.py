# import openai,requests
# openai.api_key = "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"
#
#
# prompt = "请用python flask框架写一个调用chatgpt的项目"
# model = "text-davinci-002"
#
# response = openai.Completion.create(
#     engine=model,
#     prompt=prompt,
#     max_tokens=50,
# )
# print(response.choices[0].text)
# # for xx in response.choices[0].text:
# #     print(xx)
from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# 设置OpenAI API密钥
# openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_key = "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"
# 定义路由，处理POST请求
@app.route('/chatgpt', methods=['POST'])
def chatgpt():
    # 从POST请求中获取用户输入的消息
    input_text = request.form.get('input_text')

    # 调用OpenAI的GPT-3模型生成回复
    response = openai.Completion.create(
        engine="davinci",
        # prompt=f"Conversation:\nUser: {input_text}\nAI:",
        prompt=input_text,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # 从OpenAI的回复中提取AI的回答
    ai_response = response.choices[0].text.strip()
    print(ai_response,type(ai_response))
    # 将AI的回答作为JSON格式返回给前端
    return jsonify({'response': ai_response})

# 启动Flask应用
if __name__ == '__main__':
    app.run(debug=True)
