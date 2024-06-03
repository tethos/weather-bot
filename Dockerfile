FROM python:3.9-slim

# SET UID AND GID
ARG USER_ID=1002
ARG GROUP_ID=1002
RUN addgroup --gid $GROUP_ID martin && \
    adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID martin

WORKDIR /app

USER martin

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3.9", "main.py"]
