# Start from the official Python base image.
FROM python:3.9

# Set the current working directory to /app
# This is where we'll put all the files
WORKDIR /app

# Copy all the files to the /app directory.
COPY . .

# Install the package dependencies in the requirements file.
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Set the command to run the uvicorn server.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
