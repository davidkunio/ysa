FROM python:3.6
ADD . /ysa
WORKDIR /ysa
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ['python','app.py']

