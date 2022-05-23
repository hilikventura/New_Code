#!/bin/bash

echo "Choose which folder to turn into a docker: "
read -e folder
cd $folder
echo "Choose what python file to run:"
read -e pyfile
echo "Enter arguments you'd like to give to it:(if none press enter)"
read -e args
echo "Name the new docker: (Only lowercase) "
read name
cd ..

mkdir temp
cp -r $folder/* temp/.
pipreqs temp/.
python3 cleanReqs.py temp/requirements.txt
cd temp



touch Dockerfile
echo "FROM python" > Dockerfile
echo "COPY . /home/myapp" >> Dockerfile
echo "RUN pip install -r /home/myapp/requirements.txt " >> Dockerfile
echo "EXPOSE 8000" >> Dockerfile


docker image build -t "$name" .
docker run -t -d -p 8000:8000 --name new_container "$name"

cd ..
rm -r temp
docker images
echo ""
docker ps -a

docker exec -it new_container python /home/myapp/$pyfile $args
