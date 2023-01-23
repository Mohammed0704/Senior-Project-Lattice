FROM python:3.8 

#RUN apt-get update 
#RUN apt-get install python3-pip
#RUN apt-get install flask

ADD app.py /
ADD requirements.txt /
#ADD /templates/ /templates/
ADD /code_files /code_files/
ADD /static_files /static_files/

RUN pip3 install -r requirements.txt

WORKDIR /

EXPOSE 4999

CMD ["python3", "-u", "app.py"]
