# use a python container as a starting point
FROM python:3.7-slim
WORKDIR /app
ENV HOME=/app
COPY . .
USER root

RUN apt-get update
RUN apt-get install nano
# install dependencies of interest
COPY requirements.txt requirements.txt
RUN python -m pip install rasa[full]
RUN python -m pip install -r requirements.txt
RUN python -m spacy download en_core_web_md

# set workdir and copy data files from disk
# note the latter command uses .dockerignore

# train a new rasa model
RUN rasa init --no-prompt

# set the user to run, don't run as root
EXPOSE 8000
# set entrypoint for interactive shells

# command to run when container is called to run
CMD ["python", "deploy.py"]
