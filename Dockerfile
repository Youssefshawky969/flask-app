#This is the latest official Python runtime as a base image
FROM python:3.13.0

#Set the working directory in the container
WORKDIR /app

#Copy the current directory contents into the container at /app
COPY . /app

#Install the dependencies (Flask)
RUN pip install Flask

#Expose port 5000 to the outside world
EXPOSE 5000

#Define the command to run the Flask app
CMD [ "python", "app.py" ]
