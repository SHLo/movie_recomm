rm -rf ./db/*;
docker rm -f movie_recomm;
docker run --name movie_recomm -v $(pwd)/db:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=password -d -p 127.0.0.1:3306:3306 mysql;
sleep 25;
echo 'create database MOVIE_RECOMM;' | mysql -u root -ppassword -h 127.0.0.1 -P 3306;
./manage.py migrate main 0001_initial;
