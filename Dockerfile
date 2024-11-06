# Use a base image of Python 3.9 with the "slim" variant, which is a lighter version.
FROM python:3.9-slim

# Set the working directory inside the container.
WORKDIR /app

# Copy the content of the /app directory from the host machine (outside the container) to the /app directory inside the container.
COPY /app /app/

# Install the dependencies listed in the requirements.txt file, using the --no-cache-dir option to avoid storing pip's cache,
# and the --user option to install dependencies in the user's local environment (without requiring superuser permissions).
RUN pip install --no-cache-dir --user -r requirements.txt

# Expose port 8000 for FastAPI app.
EXPOSE 8000

# Set an environment variable to disable buffering in Python, which helps log output to be shown in real time.
ENV PYTHONUNBUFFERED=1

# Define the command to run when the container starts - runs the main.py file using Python.
CMD ["python", "main.py"]