docker build -t args -f Dockerfile.arg --build-arg Flask_Ver=3.0.3 .

docker build -t args -f Dockerfile.arg --build-arg Flask_ver=3.0.3 --build_arg Python_Image_Tag=slim .

docker build -t args -f Dockerfile.label --build-arg Flask_Ver=3.0.3 --build-arg Python_Image_Tag=3.8.0a4-stretch .


docker run -it --rm -p 5000:5000 args

docker inspect args

docker history args