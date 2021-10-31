import hashlib
import os
from flask import Flask, render_template, request, jsonify, send_file

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10e8
app.config["UPLOAD_PATH"] = "store"


@app.route("/")
def index():
    return "Hello!"


@app.route("/upload", methods=["GET", "POST"])
def upload():
    """
    View for handling file upload.
    """
    if request.method == "POST":
        uploaded_file = request.files["file"]
        content = uploaded_file.read()
        file_hash = hashlib.md5(content).hexdigest()
        path_to_file = os.path.join(app.config["UPLOAD_PATH"], file_hash[:2])
        os.makedirs(path_to_file, exist_ok=True)
        with open(f"{path_to_file}/{file_hash}", "wb+") as storage:
            storage.write(content)
        return jsonify(file_hash=file_hash)
    return render_template("index.html")


@app.route("/download")
def download():
    """
    View for handling file download.
    """
    file_hash = request.args.get("hash")
    if not file_hash:
        return "Please, provide hash to download file."
    path = os.path.join(app.config["UPLOAD_PATH"], file_hash[:2], file_hash)
    try:
        return send_file(path, as_attachment=True)
    except FileNotFoundError:
        return "This file doesn't exist."


@app.route("/delete", methods=["DELETE"])
def delete():
    """
    View for handling file deletion.
    """
    file_hash = request.args.get("hash")
    if not file_hash:
        return "Please, provide hash to delete file."
    path_to_file = os.path.join(app.config["UPLOAD_PATH"], file_hash[:2], file_hash)
    if os.path.exists(path_to_file):
        os.remove(path_to_file)
        return "Successfully deleted."
    return "This file doesn't exist."


if __name__ == "__main__":
    app.run(debug=True)
