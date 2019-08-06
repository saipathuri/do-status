FROM python:alpine

WORKDIR /usr/src/app

RUN apk update && apk add gcc python3-dev musl-dev linux-headers
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ ./

# CMD [ "python", "./main.py" ]