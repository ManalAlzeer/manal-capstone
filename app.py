import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth.auth import AuthError, requires_auth
from sqlalchemy import func

from models import setup_db, Movie, Actor

def create_app(test_config=None):
  app = Flask(__name__)
  setup_db(app)

  # CORS(app)
  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

  '''
    GET /movies

  '''
  @app.route('/movies', methods=['GET'])
  @requires_auth('get:movies')
  def get_movies(payload):
    movies = Movie.query.all()

    if len(movies) == 0:
      abort(404)

    return jsonify({
      'success': True,
      'movies': [movie.format() for movie in movies]
    }), 200


  '''
   GET /Actors

  '''
  @app.route('/actors', methods=['GET'])
  @requires_auth('get:actors')
  def get_actors(payload):
    Actors = Actor.query.all()

    if len(Actors) == 0:
      abort(404)

    return jsonify({
      'success': True,
      'actors': [actor.format() for actor in Actors]
    }), 200


    
  '''
  POST /movies, 
 
  '''
  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movies')
  def create_movies(payload):

    body = request.get_json()
    title = body.get('title')
    release = body.get('release')
    
    try:
        movie = Movie(title=title, release=release)
        movie.insert()
    
        return jsonify({
          'success': True,
          'created': movie.id,
          })

    except:
        abort(400)
  

  '''
  POST /Actors, 
 
  '''
  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actors')
  def create_actors(payload):

    body = request.get_json()
    name = body.get('name')
    age = body.get('age')
    gender = body.get('gender')
    
    try:
        actor = Actor(name=name, age=age, gender=gender)
        actor.insert()
    
        return jsonify({
          'success': True,
          'created': actor.id,
          })

    except:
        abort(400)



  '''
  DELETE /movie
  '''
  @app.route('/movies/<int:id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movie(payload, id):

    try:
      movie = Movie.query.filter(Movie.id == id).one_or_none()

      if movie is None:
        abort(404)

      movie.delete()

      return jsonify({'success': True, 'delete': id}), 200

    except:
      abort(422)

  '''
  DELETE /actor
  '''
  @app.route('/actors/<int:id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actors(payload, id):

    try:
      actor = Actor.query.filter(Actor.id == id).one_or_none()

      if actor is None:
        abort(404)

      actor.delete()

      return jsonify({'success': True, 'delete': id}), 200

    except:
      abort(422)

  '''
    PATCH /movies
  '''
  @app.route('/movies/<int:id>', methods=['PATCH'])
  @requires_auth("patch:movies")
  def update_movie(payload, id):

    data = request.get_json()
    movie = Movie.query.filter(Movie.id == id).one_or_none()

    if not movie:
        abort(404)
    try:
        movie.title = data.get('title')
        movie.release = data.get('release')
        movie.update()
    except:
        abort(400)
        
    return jsonify({
        'success': True,
         }), 200

  '''
    PATCH /actor
  '''
  @app.route('/actors/<int:id>', methods=['PATCH'])
  @requires_auth("patch:actors")
  def update_actors(payload, id):

    data = request.get_json()
    actor = Actor.query.filter(Actor.id == id).one_or_none()

    if not actor:
        abort(404)
    try:
        actor.name = data.get('name')
        actor.age = data.get('age')
        actor.gender = data.get('gender')
        actor.update()
    except:
        abort(400)
        
    return jsonify({
        'success': True,
         }), 200



  '''
error handlers for all expected errors 


  '''
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False, 
      "error": 404,
      "message": "resource not found"
      }), 404
  
  @app.errorhandler(405)
  def not_found(error):
    return jsonify({
      "success": False, 
      "error": 405,
      "message": "method not allowed"
      }), 405

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False, 
      "error": 422,
      "message": "unprocessable"
      }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False, 
      "error": 400,
      "message": "bad request"
      }), 400

  @app.errorhandler(500)
  def not_found(error):
    return jsonify({
      "success": False, 
      "error": 500,
      "message": "internal server error"
      }), 500

  @app.errorhandler(AuthError)
  def auth_error(error):
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error['description']
    }), error.status_code

  
  return app

app = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)