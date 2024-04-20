# Use an official Python runtime as a parent image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY python_app.py /app/

COPY random_paragraphs.txt /app/
# Install any dependencies required by the Python script
RUN pip install nltk

# Download NLTK resources (stopwords and punkt tokenizer)
RUN python -m nltk.downloader stopwords punkt

# Run the Python script when the container launches
CMD ["python", "python_app.py"]
