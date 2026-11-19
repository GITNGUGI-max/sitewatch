FROM python:3.13-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY check_website.py dashboard.py ./

COPY templates/ ./templates/
COPY static/ ./static/

CMD [ "python", "check_website.py" ]
