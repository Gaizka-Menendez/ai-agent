# Declare what image to use 
# FROM image_name:latest
FROM python:3.13.7-slim-trixie

WORKDIR /app

# COPY local_folder container_folder
# RUN mkdir -p /static_folder
# same destination is /app
COPY ./src .

# RUN echo "hello" > index.html

# docker buildx build -f Dockerfile -t pyapp .
# docker run -t pyapp

# docker buildx build -f Dockerfile -t gaizkam/ai-pyapp-test:latest .
# docker push gaizkam/ai-pyapp-test:latest

# python -m http.server 8000
# docker run -it -p 3000:8000 
CMD ["python", "-m", "http.server", "8000"]