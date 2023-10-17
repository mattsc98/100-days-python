from flask import Flask, render_template, request
from PIL import Image
from colorthief import ColorThief

app = Flask(__name)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if "file" not in request.files:
        return "No file part"
    
    file = request.files["file"]

    if file.filename == "":
        return "No selected file"
    
    if file:
        image = Image.open(file)
        color_thief = ColorThief(image)
        dominant_color = color_thief.get_color(quality=1)
        return f"Most common color: {dominant_color}"

if __name__ == "__main__":
    app.run(debug=True)
