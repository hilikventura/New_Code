#!/bin/bash

echo "Choose which folder to turn into a docker: "
read -e folder
cd $folder
echo "Choose what python file to run:"
read -e file
echo "Name the new docker: (Only lowercase) "
read name
cd ..

mkdir temp
cp -r $folder/* temp/.
cd temp
#pipreqs .

touch Dockerfile
echo "FROM python" > Dockerfile
echo "COPY . /home/myapp" >> Dockerfile
echo "RUN pip install flask" >> Dockerfile
echo "RUN pip install requests" >> Dockerfile
#echo "RUN pip install -r /home/myapp/requirements.txt " >> Dockerfile
echo "EXPOSE 8000" >> Dockerfile
echo "RUN python /home/myapp/$file" >> Dockerfile


docker build -t "$name" .
docker run -t -d -p 8000:8000 --name "$name" "$name"
docker ps -a

cd ..

rm -r temp

