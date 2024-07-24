from python:3.10-alpine

WORKDIR /test_opencart

COPY requirements.txt ./

RUN pip install -U pip
RUN pip install -r requirements.txt
RUN mkdir screen_shot

COPY ./ ./

CMD [ "pytest", "--browser", "chrome", "--url", "http://localhost:8080/", "--executor", "172.0.0.1" ]