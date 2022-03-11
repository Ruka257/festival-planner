#use python 3.8 or latest, whichever is lower
FROM python:3.8
# Copy contents into image
WORKDIR /festival-app
COPY . .
# Set environment variables; test env empty sqlite db
ENV DATABASETEST_URI=${DATABASETEST_URI}
ENV DATABASE_URI=${DATABASE_URI}
# install pip dependencies from requirements.txt
RUN pip3 install -r requirements.txt
# Expose correct port
EXPOSE 5000
# Create an entrypoint