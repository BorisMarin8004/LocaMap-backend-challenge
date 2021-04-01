FROM python:3.8

EXPOSE 5000

# Tell python to not generate .pyc
ENV PYTHONDONTWRITEBYTECODE 1

# Turn off buffering
ENV PYTHONUNBUFFERED 1

ADD requirements.txt .

RUN python -m pip install -r requirements.txt

WORKDIR /backend
ADD . /backend
CMD ["flask", "run"]