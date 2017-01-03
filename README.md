# movie_recomm
A fullstack app for movie recommendation based on collaborative filtering technique

## Installation
```sh
$ git clone https://github.com/SHLo/movie_recomm.git
create a virtual environment for python 2.7 (recommended)
$ pip install -r requirements.txt; pip install --upgrade --no-cache-dir https://get.graphlab.com/GraphLab-Create/2.1/shlo.sam@gmail.com/6618-0B15-97AF-BE03-F5B0-B01A-DDC6-5FBF/GraphLab-Create-License.tar.gz;
$ cd static; npm install; npm run build; (node 4.4.7)
launch a mysql server on localhost:3306, create a DB named "MOVIE_RECOMM"
change to the root directory, $ python manage.py migrate main; python manage.py migrate; (it may take a while for movie poster image crawling)
```

## Usage
```sh
change to the root directory, $ python manage.py runserver;
```

0. visit "localhost:8000/index" at your browser for a guest tour
1. register an account by email and start rating movies
2. click the switch button to check your rating history
3. the recommender app combines your rating with others to generate a recommendation list for you
