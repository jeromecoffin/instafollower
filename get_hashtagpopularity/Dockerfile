FROM python:latest

WORKDIR /usr/app/src

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY get_hashtagpopularity.py .

ENV HASHTAG="moderesponsable"

CMD ["python", "get_hashtagpopularity.py", "${HASHTAG}"]