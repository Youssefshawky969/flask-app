# Use a specific version for consistency
FROM python:3.13.0 AS builder

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file first for caching purposes
COPY requirements.txt .

#Install the dependencies (Flask)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Use a smaller image for the final stage
FROM python:3.8.0-slim 

#Set the working directory in the container
WORKDIR /app

# Copy installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=builder /app /app

#Expose port 5000 to the outside world
EXPOSE 5000

#Define the command to run the Flask app
CMD [ "python", "app.py" ]
