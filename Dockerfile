FROM python:3.10-alpine
WORKDIR /service
RUN apk add --no-cache --update \
    python3 python3-dev gcc \
    gfortran musl-dev g++ \
    libffi-dev openssl-dev \
    libxml2 libxml2-dev \
    libxslt libxslt-dev \
    libjpeg-turbo-dev zlib-dev
RUN pip install --upgrade pip
RUN pip install --upgrade cython
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . ./
EXPOSE 8084
ENTRYPOINT [ "python","main.py" ]