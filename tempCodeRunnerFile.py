@app.route("/files/<path:file_path>")
def file_path(file_path):
    return file_path
