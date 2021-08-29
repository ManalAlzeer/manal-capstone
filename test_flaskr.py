import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movie, Actor


class CapstoneTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = 'postgresql://postgres:admin@localhost:5432/capstone'
        setup_db(self.app, self.database_path)
        
        self.Executive_Producer = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjdicDBaN3JhNldxVE45elJWV1ByMyJ9.eyJpc3MiOiJodHRwczovL21hbmFsLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MTI5NmRkZGFhYWIyZjAwNmFlMDczZWYiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYzMDE5MTQ2NCwiZXhwIjoxNjMwMTk4NjY0LCJhenAiOiJGWjkwS0huUndkY2hVMkpjMEVMVzljRmlJQjZvSFpubCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.ZkEXs7JHmX9mRl4W0QwIk1b_rj8GMwXYvsgDzk4WWmO-77ddvphai3Ny6OnwX9YKzPfh-FOYJbwm4kiRowBTAcys4pGoNMqztCEP1YLwECEVe1Ll9Hm-JhkUYvDq2q-alTxY7HXhEiWn-CmpSA4C6SMd8eszdKojwk9i12FoD4-WdXI_EhRnL9K08nz5fGOkYHAJExxQpf56LqQDMDPJ2YVevwy_wKSOvB5EQQTtrcvMur4y46iwVsglVbTcg-rZTSmnKKMdS33_GzjcQnH5EZKLmF9ab7nE5AGvVqNEZRRw7wwipGRgTSZ4QOem4K4yKaNhWv7EKN2rrDkLdwf9TA'
        # self.Casting_Director = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjdicDBaN3JhNldxVE45elJWV1ByMyJ9.eyJpc3MiOiJodHRwczovL21hbmFsLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNTQ3NTY0ODExOTUzMjU4MzMzMCIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNjMwMTA1ODI0LCJleHAiOjE2MzAxMTMwMjQsImF6cCI6IkZaOTBLSG5Sd2RjaFUySmMwRUxXOWNGaUlCNm9IWm5sIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.grNrpyCryL64ROFtPdhCT_oNgbdRTSsWkOqnA8eVG17bJ3OC_nw_0TPwXaIPU4YQEsG2U6x9zSakkZjs5xsroAIyma7ckyUSp8kkzUMwdLC8XB1mXERFVKdWVG7ye61WAwyk-2MNdof_sLj2CYyx5MC0oZ3FbqAPwj1RulLt4_F2fOpqJGV77qcmji-aICUbtqDVO3NBtLc8UNNI8GzP2PAmfX_bMgcZNc7-oE253zygRfG878UAbOIF5SToctDRSA95RnbbZH6jNoYUBG0_Y7fUzeYlj5Cp2gKzlxoDS2l549E40ITR7bxPnRpaMBM2CoEbVA-i755ZUhXaHMmn0w'
        # self.Casting_Assistant = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjdicDBaN3JhNldxVE45elJWV1ByMyJ9.eyJpc3MiOiJodHRwczovL21hbmFsLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MTA5ODgzZmM3MjQwNTAwNzFiNmVhOTciLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYzMDEwNTQ2MCwiZXhwIjoxNjMwMTEyNjYwLCJhenAiOiJGWjkwS0huUndkY2hVMkpjMEVMVzljRmlJQjZvSFpubCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.MYRD91xfAbp8JGM6EH-G4Kv147UsTKRs108t4YE0HIMgzk3bJE_QYPC_q1hLa1SPOqgrHTdCmczL0Rv4q-GXEh6o7DNZp77k6S3kkLRFLt39QaFJ_k_0MWUsf_zVlHLZvPJa-kbkQESLAbQ8YcCEmA9foEauEprScpb63VHPSxuc5_ydEiibuP2hjOT8sWrb0z9l0NDaoS37eZDNuxooszCnuUQq8fCOYyxUWnGaKVyk1K448wE_MUcD5YDq8qTYJWTZMeA7vxxvUNVOgAxb8lacu47pvQtN-zKeYDylqML0cb4JC4Wzmh_gYNOlwcMUe5WjVkoUWO8WZT_ne_Di4w'

        self.movie = {
            "title": "Mousa",
            "release": "2021-08-02"
        }

        self.actor = {
            "name": "Matthew McConaughey",
            "age": 51,
            "gender": 'Male'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()


    
    def tearDown(self):
        """Executed after reach test"""
        pass


# Get movies & actors with permission
    def test_get_actors(self):
        res = self.client().get('/actors',headers={'Authorization': 'Bearer ' + self.Executive_Producer})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))
    
    def test_get_movies(self):
        res = self.client().get('/movies',headers={'Authorization': 'Bearer ' + self.Executive_Producer})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

# Get movies & actors without_permission
    def test_get_actors_without_permission(self):
        res = self.client().get('/actors')
        self.assertEqual(res.status_code, 401)
    
    def test_get_movies_without_permission(self):
        res = self.client().get('/movies')
        self.assertEqual(res.status_code, 401)


# Delete movies & actors with premission
    def test_delete_actor(self):
        res = self.client().delete('/actors/4',headers={'Authorization': 'Bearer ' + self.Executive_Producer})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
    
    def test_delete_movies(self):
        res = self.client().delete('/movies/4', headers={'Authorization': 'Bearer ' + self.Executive_Producer})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

# Delete movies & actors without premission
    def test_delete_actor_without_permission(self):
        res = self.client().delete('/actors/2')
        self.assertEqual(res.status_code, 401)
    
    def test_delete_movies_without_permission(self):
        res = self.client().delete('/movies/2')
        self.assertEqual(res.status_code, 401)

# Delete movies & actors fail
    def test_delete_actor_fail(self):
        res = self.client().delete('/actors/1000')
        self.assertEqual(res.status_code, 401)

    def test_delete_movies_fail(self):
        res = self.client().delete('/movies/1000')
        self.assertEqual(res.status_code, 401)

# Create movies & actors with premission
    def test_create_movies(self):
        res = self.client().post('/movies',json={'title': 'Luca', 'release': '2021-03-20'}, headers={'Authorization': 'Bearer ' + self.Executive_Producer})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_create_actors(self):
        res = self.client().post('/actors',json={'name': 'Leonardo Di Caprio', 'age': '46' , 'gender':'male'},  headers={'Authorization': 'Bearer ' + self.Executive_Producer})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])


# Create movies & actors without_permission
    def test_create_movies_without_permission(self):
        res = self.client().post('/movies',json={'title': 'Luca', 'release': '2021-03-20'})
        self.assertEqual(res.status_code, 401)

    def test_create_actors_without_permission(self):
        res = self.client().post('/actors',json={'name': 'Leonardo Di Caprio', 'age': '46' , 'gender':'male'})
        self.assertEqual(res.status_code, 401)


# update movies & actors 
    def test_patch_movie(self):
        res = self.client().patch('/movies/6', json=self.movie, headers={'Authorization': 'Bearer ' + self.Executive_Producer})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        
    def test_patch_actor(self):
        res = self.client().patch('/actors/5', json=self.actor ,headers={'Authorization': 'Bearer ' + self.Executive_Producer})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

# Update movies & actors fail
    def test_patch_movie_fail(self):
        res = self.client().patch('/movies/patch/2000', json=self.movie)
        self.assertEqual(res.status_code, 404)

    def test_patch_actor_fail(self):
        res = self.client().patch('/actors/patch/2000', json=self.actor)
        self.assertEqual(res.status_code, 404)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()