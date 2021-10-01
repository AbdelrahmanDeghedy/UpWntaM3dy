# from models.auth.authModels import db


# db.create_all()

from app import createApp

app = createApp()

if __name__ == '__main__':
    app.run(debug=True, port=5000)