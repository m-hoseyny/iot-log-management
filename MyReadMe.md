
Base directory for develpment is: 
./backend/app

To do migration
```
alembic upgrade head
```

To init db with superuser
```
python app/initial_data.py
```

To start the program:
```
uvicorn app.main:app --reload
```