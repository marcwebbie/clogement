import datetime
from flask import Flask, url_for
from flask.ext import restful, mongoengine


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "test"}
app.config["SECRET_KEY"] = "K33pThisS3cr3t"
api = restful.Api(app)
db = mongoengine.MongoEngine(app)


class Post(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True)
    body = db.StringField(required=True)
    comments = db.ListField(db.EmbeddedDocumentField('Comment'))

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }


class Comment(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(verbose_name="Comment", required=True)
    author = db.StringField(verbose_name="Name", max_length=255, required=True)



import pudb; pudb.set_trace()


class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(debug=True)
