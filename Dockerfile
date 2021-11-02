FROM python:3.9

WORKDIR /app

ARG SENTRY_RELEASE_ID
ENV SENTRY_RELEASE_ID ${SENTRY_RELEASE_ID:-""}

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./upman .

EXPOSE 8080

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8080", "--workers", "4", "--threads", "2", "application:create_app()"]