export FLASK_ENV=development
export FLASK_APP=flasktest.py
flask run

cd
cd mongodb/bin
./mongod -f m.conf