FROM python:3.8-slim-buster

EXPOSE 81

COPY requirements.txt .

RUN apt-get update && apt-get -y install gcc dnsutils

RUN --mount=type=cache,target=/root/.cache/pip  python -m pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "infilectProject.wsgi:application", "--workers", "5", "--timeout", "360", "-b"  ,"0.0.0.0:81"]