import sys
sys.path.insert(0, './utils')

from flask import Flask, render_template, request, jsonify, send_file
import pdfplumber
import io
from translate import Translator
from utils import textToVideo

app = Flask(__name__)

@ app.route('/')
def index():
    return render_template('index.html')


@ app.route('/upload', methods=['POST'])
def upload():
    if 'pdfFile' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    pdf_file = request.files['pdfFile']

    if pdf_file.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        with pdfplumber.open(io.BytesIO(pdf_file.read())) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
            
            video_path = textToVideo.create_video_from_text(
                get_path=r'D:\Programs Related\Team Project\gdsc-project',
                folder_path=r'D:\Programs Related\Team Project\gdsc-project\out',
                text=text,
                audio_path="out\\file\\output.mp3",
                video_path="out\\file\\output.mp4"
            )

            print(video_path)

            return send_file(video_path, mimetype="video/mp4")
            

        #     # Translate to Tamil
        #     tamil_text = Translator(to_lang='ta').translate(text)

        #     # Translate to Hindi
        #     hindi_text = Translator(to_lang='hi').translate(text)

        #     # Translate to Telugu
        #     telugu_text = Translator(to_lang='te').translate(text)

        #     # Translate to Bengali
        #     bengali_text = Translator(to_lang='bn').translate(text)

        #     # Translate to Marathi
        #     marathi_text = Translator(to_lang='mr').translate(text)

        #     # Translate to Kannada
        #     kannada_text = Translator(to_lang='kn').translate(text)

        # return jsonify({
        #     'tamil': tamil_text,
        #     'hindi': hindi_text,
        #     'telugu': telugu_text,
        #     'bengali': bengali_text,
        #     'marathi': marathi_text,
        #     'kannada': kannada_text
        # })
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
