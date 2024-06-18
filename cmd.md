docker build -t args -f Dockerfile.arg --build-arg Flask_Ver=3.0.3 .

docker run -it --rm -p 5000:5000 args

docker inspect args

docker history args