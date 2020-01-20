from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import request
from flask import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post ' + str(self.id)
        



all_posts = [
    {
        'title': 'post 1',
        'content': 'This is my new feeds 1',
        'author': 'rouen'
    },
    {
        'title': 'post 2',
        'content': 'This is my new feeds 2'
    }
]

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/post', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/post')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('post.html', posts=all_posts)

@app.route('/onlyget', methods=['GET','POST'])
def get_req():
    return 'Rouen Pro'

@app.route('/post/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/post')

@app.route('/post/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    post = BlogPost.query.get_or_404(id)
    if request.method == 'POST':
        
        post.title = request.form['title']
        post.content = request.form['content']
        post.author = request.form['author']
        db.session.commit()
        return redirect('/post')

    else: 
        return render_template('edit.html', post=post)

if __name__ == "__main__":
    app.run(debug=True)
