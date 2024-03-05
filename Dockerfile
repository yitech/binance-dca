# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /dca

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir python-binance

# Define environment variable
ENV API_KEY api_key
ENV API_SECRET api_secret

# Run script.py when the container launches
CMD ["python", "./main.py"]
