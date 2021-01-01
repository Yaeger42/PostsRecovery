FROM python:3 
ENV PYTHONBUFFERED=1
WORKDIR /blog
COPY requirements.txt /blog/
RUN pip install -r requirements.txt 
COPY . /blog/ 