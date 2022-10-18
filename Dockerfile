FROM python:alpine
# pass --build-arg FORCE_ERROR=yes to force the build to fail
ARG FORCE_ERROR=""
WORKDIR /app/

# Placeholder to test network sandboxing
# RUN curl https://www.google.co.jp/
COPY requirements.txt .
RUN pip install -Ur requirements.txt
COPY . .


RUN if [[ $FORCE_ERROR = "yes" ]]; then exit 1; fi


ENTRYPOINT ["python", "main.py"]