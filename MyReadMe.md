
Base directory for develpment is: 
./backend/app

To run poetry
```
poetry install
poetry update
```

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


To create new migration file!
```
alembic revision --autogenerate -m "MIGRATION NAME"
```

Thingsboard Schema
```
https://github.com/thingsboard/thingsboard/blob/master/dao/src/main/resources/sql/schema-entities.sql
```

How system works?

1. Make one device first
2. Create a device credential until the device can verify
