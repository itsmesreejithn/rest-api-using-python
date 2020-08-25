from flask import Flask 
from flask_restful import Api , Resource , reqparse
from flask_sqlalchemy import SQLAlchemy , Model

app = Flask(__name__)
api = Api(app)
app.config[SQLAlchemy_DATABASE_URI] = 'sqlite:///tmp/database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(100) , nullable=False)
    views = db.Column(db.Integer , nullable=False)
    likes = db.Column(db.Integer , nullable=False)

    def __repr__(self):
        return f"Video(name={name}, views={views}, likes={likes}"


db.create_all() #intitialize the atabase also run only once

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name" , type=str , help="Name of video" , required=True)
video_put_args.add_argument("views" , type=str , help="Views of video" , required=True)
video_put_args.add_argument("likes" , type=str , help="Likes of video" , required=True)

videos = {}

def a_i_vi_d_e(video_id):                       #abort if video id doesnot exist
    if video_id not in videos:
        abort(404 , message="Video id is not valid.......")

def a_i_vi_e(video_id):                         #abort if video id exist
    if video_id in videos:
        abort(409 , message="Video already exist with that id......")


class Video(Resource):
    def get(self,video_id):
        a_i_vi_d_e(video_id)
        return videos[video_id]

    def put(self , video_id):
        a_i_vi_e(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id] , 201 #created the video

    def delete(self , video_id):
        a_i_vi_d_e(video_id)
        del videos[video_id]
        return '' , 204


api.add_resource(Video , "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug = True)