FROM python:3.10   

EXPOSE 8000

COPY requirements.txt .

RUN apt-get update && apt-get -y install gcc dnsutils

RUN --mount=type=cache,target=/root/.cache/pip  python -m pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver"]
