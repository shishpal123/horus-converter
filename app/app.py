from flask import Flask, request, render_template, send_file, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename

from app.converters.csv_to_horus import convert_csv_to_horus
from app.converters.json_to_horus import convert_json_to_horus
from app.converters.image_to_horus import convert_image_to_horus
from app.converters.audio_to_horus import convert_audio_to_horus
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
CONVERTED_FOLDER = os.path.join(BASE_DIR, 'converted')

ALLOWED_EXTENSIONS = {'csv', 'json', 'png', 'wav'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONVERTED_FOLDER'] = CONVERTED_FOLDER
app.secret_key = 'secret_key'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file or file.filename == '':
            flash('No file selected!')
            return redirect(request.url)

        if not allowed_file(file.filename):
            flash('Unsupported file type!')
            return redirect(request.url)

        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(input_path)

        ext = filename.rsplit('.', 1)[1].lower()
        base_name = filename.rsplit('.', 1)[0]
        output_filename = base_name + '_horus.csv'
        output_path = os.path.join(app.config['CONVERTED_FOLDER'], output_filename)

        try:
            if ext == 'csv':
                convert_csv_to_horus(input_path, output_path)
            elif ext == 'json':
                convert_json_to_horus(input_path, output_path)
            elif ext == 'png':
                convert_image_to_horus(input_path, output_path)
            elif ext == 'wav':
                convert_audio_to_horus(input_path, output_path)
            else:
                flash('File type not supported')
                return redirect(request.url)

            return send_file(output_path, as_attachment=True)
        except Exception as e:
            import traceback
            traceback.print_exc()
            flash(f'Conversion error: {str(e)}')
            return redirect(request.url)

    return render_template('index.html')

