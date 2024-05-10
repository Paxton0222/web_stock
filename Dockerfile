FROM python:3.10.9-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY Pipfile Pipfile.lock ./
RUN apk update && \
    apk add git && \
    pip install pipenv && \
    pipenv --python `which python3` && \
    pipenv install --system --deploy  && \
    pipenv run twstock -U && \
    apk --purge del apk-tools

COPY . .
EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
