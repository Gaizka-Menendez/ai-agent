FROM python:3.13.7-slim-trixie

# Creating python virtual environment, isolate python from system-leven python
RUN python -m venv /opt/venv
ENV PATH=/opt/venv/bin:$PATH

WORKDIR /app

# COPY local_folder/file container_destination
COPY requirements.txt /tmp/requirements.txt

# RUN pip install -r /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY ./src .

CMD ["python", "-m", "http.server", "8000"]