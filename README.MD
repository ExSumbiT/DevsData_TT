## Test task for SheepFish company

Used:

```
 - Django
 - Django REST Framework
 - SQLite3
```

Usage:

```
git clone https://github.com/ExSumbiT/DevsData_TT.git
cd DevsData_TT
pip install -r requirements.txt
```

Apply migrations and load Events fixtures:

```
cd MagicEvents
python manage.py migrate
python manage.py loaddata events.json
```

Run django server:

```
cd SheepFish
python manage.py runserver
```