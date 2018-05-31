from signalapp import db
from signalapp.models import User

db.create_all()


admin = User(email='admin@signalway.com', password='test')
db.session.add(admin)
db.session.commit()