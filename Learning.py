# run a vritual environment

print('''
source venv/bin/activate
!pip install Flask
python -m flask --version
python venv/hello.py
export FLASK_APP=hello.py
export FLASK_ENV=development
flask run

// fusing a port
sudo fuser -k xxxx/tcp
''')