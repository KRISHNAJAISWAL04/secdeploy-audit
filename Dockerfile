# Use a lightweight, secure Linux baseline image
FROM python:3.11-slim

# Set up a secure working directory inside the container
WORKDIR /app

# Copy the scanner script into the container image
COPY audit.py .

# Define the default command to execute when the container launches
CMD ["python", "audit.py"]
