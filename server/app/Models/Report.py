from .database import db

class Report(db.Model):
    __tablename__ = 'reports'
    id = id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    #title will be chosen from a list of report titles (predefined)
    title = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return '<Report %r' % self.title