docker build -t args -f Dockerfile.arg --build-arg Flask_Ver=3.0.3 .
docker build -t args-3.0.3 -f Dockerfile.arg --build-arg Flask_ver=$VER --build-arg Python_Image_Tag=slim .

docker run -it --rm -p 5000:5000 args-3.0.3

docker inspect args

docker history args

set VER=3.0.3
set NAME=args-3.0.3 