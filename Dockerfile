# Use an official Python runtime as the base image
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY simple_time_service.py .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define the command to run the application
CMD ["python", "simple_time_service.py"]
