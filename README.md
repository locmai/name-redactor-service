# Name Redactor Service

![Build Docker image on Push to Feature branches](https://github.com/locmai/name-redactor-service/workflows/Build%20Docker%20image%20on%20Push%20to%20Feature%20branches/badge.svg)

## Quickstart with Docker

```bash
docker run --rm -p 8000:8000 locmai/name-redactor-service:0.1.0
```

To try out the service, please go to http://localhost:8000/docs for API docs or use Postman to send the GET request (fetch from the given source) or POST request with the JSON body.

## Task 1: Build a service to redact the names of the people from JSON data

- Assuming we might have an NLP service to detect human's name in the data. I used [spaCy](https://spacy.io/) library with their default model for English. - The real model should be trained by a different process and store in cloud storage like S3 or Azure Storage and mounted to the container at runtime to minimize the Docker image and separate the concerns of NLP model with business logic.
- Implemented two methods, GET request (fetch from the given [source](http://therecord.co/feed.json)) or POST request with the JSON body using [fastAPI](https://fastapi.tiangolo.com/) framework - which I found it was similar to Flask but faster and more handy tools were given.
- I tried to recursively handle the JSON data which led to slow performance. Another solution could be parsing all the data to string and replace them all.
-

## Task 2: Package the service & deploy to a k8s cluster

- Packaged the service with Docker.
- Wrote a simple Helm chart for deploying the service to k8s.
- Initialized Skaffold skeleton for development enviroment and production

## Task 3: CI strategy for your service
