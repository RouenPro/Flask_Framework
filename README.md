# Flask_Framework
Learning Flask Framework
sodu pip3 install flask
sudo pip install virtualenv  
virtualenv yourenv -p python3
source yourenv/bin/activate   


Install database on flask
Pip install flask-sqlalchemy


//Problem of db error just move db to under app.config
from app import db
db.create_all()
from app import BlogPost
BlogPost.query.all()
db.session.add(BlogPost(title='Blog Post 1', content='content of blog page 1', author='Puraro'))
BlogPost.query.all()
BlogPost.query.all()[1].content
