from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    all_posts = get_blogs()
    return render_template("index.html", all_posts=all_posts)

def get_blogs():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()    
    
    post_data = [Post(post['id'], post['title'], post['subtitle'], post['text']) for post in all_posts]
        
    return post_data

@app.route('/posts/<int:id>')
def full_post(id):
    all_posts = get_blogs()
    data = ''
    for post in all_posts:
        if id == post.id:
            data = post 
    
    return render_template("post.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
