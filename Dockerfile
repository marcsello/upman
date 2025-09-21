FROM python:3.13

WORKDIR /app

ARG SENTRY_RELEASE_ID
ENV SENTRY_RELEASE_ID ${SENTRY_RELEASE_ID:-""}

COPY requirements.txt entrypoint.sh ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./upman .

EXPOSE 8080

ENTRYPOINT ["/bin/sh", "entrypoint.sh"]