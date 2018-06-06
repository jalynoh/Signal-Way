from signalapp import db
from signalapp.models import User
from signalapp import bcrypt

db.create_all()


hashed_password = bcrypt.generate_password_hash('test').decode('utf-8')
admin = User(first_name='test', last_name='account', role='admin', email='admin@signalway.com', password=hashed_password)
db.session.add(admin)
db.session.commit()