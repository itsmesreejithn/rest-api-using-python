from flask import Flask 
from flask_restful import Api , Resource , reqparse , abort , fields , marshal_with
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


db.create_all() #intitialize the database also run only once

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name" , type=str , help="Name of video" , required=True)
video_put_args.add_argument("views" , type=str , help="Views of video" , required=True)
video_put_args.add_argument("likes" , type=str , help="Likes of video" , required=True)

video_uodate_args = reqparse.RequestParser()
video_upate_args.add_argument("name" , type=str , help="Name of video")
video_update_args.add_argument("views" , type=str , help="Views of video")
video_update_args.add_argument("likes" , type=str , help="Likes of video")


resource_fields = {
    'id' : fields.Integer,
    'name' : fields.String,
    'views' : fields.Integer,
    'likes' : fields.Integer
}

def a_i_vi_d_e(video_id):                       #abort if video id doesnot exist
    if video_id not in videos:
        abort(404 , message="Video id is not valid.......")

def a_i_vi_e(video_id):                         #abort if video id exist
    if video_id in videos:
        abort(409 , message="Video already exist with that id......")


class Video(Resource):
    @marshal_with(resource_field)              #serialising into json format
    def get(self,video_id):
       result = VideoModel.query.filter_by(id = video_id).first()
       if not result:
           abort(404 , message="Could not find video with that id")
        return result

    @marshal_with(resource_fields)
    def put(self , video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409 , message="video id taken.......")
        video = VideoModel(id = video_id , name = args['name'] , views = args['views'] , likes = args['likes'])
        db.session.add(video)
        db.session.commit()
        return video , 201                      #created the video

    def patch(self , video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()        
        if not result:
            abort(404 , message="Video does not exist , cannot update")
        
        if args['name']:
        result.name = args['name']
        if args['views']:
        result.name = args['views']
        if args['likes']:
        result.name = args['likes']
        
        db.session.commit()

        return result

    def delete(self , video_id):
        a_i_vi_d_e(video_id)
        del videos[video_id]
        return '' , 204


api.add_resource(Video , "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug = True)