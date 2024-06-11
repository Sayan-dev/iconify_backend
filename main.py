import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
# from openai import OpenAI
load_dotenv()





app = Flask(__name__)



# @app.route('/generate-image', methods=['POST'])
# def get_image():
#     data = request.json
#     prompt = data.get('prompt')
#     if not prompt:
#         return jsonify({"error": "No prompt provided"}), 400

#     try:
#         response = client.images.generate(
#         model="dall-e-3",
#         prompt="a white siamese cat",
#         size="1024x1024",
#         quality="standard",
#         n=1,
#         )

#         image_url = response.data[0].url
#         return {image_url}
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

import app
server = app.create_app()

if __name__ == '__main__':
    server.run(host='127.0.0.1', port=5000, debug=True,  threaded=True)


