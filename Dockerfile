FROM python
COPY . /home/myapp
RUN pip install -r /home/myapp/requirements.txt 
EXPOSE 8000
