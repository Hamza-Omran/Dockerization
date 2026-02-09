# Text Analysis with Docker

A containerized Python application that performs text analysis on large text files using NLTK (Natural Language Toolkit). The application reads text from a file, removes common English stop words, and counts the frequency of unique words.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Docker Configuration](#docker-configuration)
- [Output](#output)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project demonstrates the use of Docker to containerize a Python application that performs natural language processing. It analyzes a text file containing random paragraphs, filters out stop words, and produces a frequency count of all meaningful words.

## Features

- **Text Analysis**: Processes large text files (8MB+ supported)
- **Stop Word Filtering**: Removes common English stop words using NLTK
- **Word Tokenization**: Breaks down text into individual words
- **Frequency Counting**: Counts occurrences of each unique word
- **Dockerized**: Fully containerized for consistent execution across platforms
- **Lightweight**: Uses Alpine Linux base image for minimal footprint

## Prerequisites

Before running this application, ensure you have the following installed:

- **Docker** (version 20.10 or higher recommended)
  - [Install Docker on Linux](https://docs.docker.com/engine/install/)
  - [Install Docker on Windows](https://docs.docker.com/desktop/install/windows-install/)
  - [Install Docker on Mac](https://docs.docker.com/desktop/install/mac-install/)

## Project Structure

```
Dockerization-main/
├── Dockerfile              # Docker container configuration
├── python_app.py          # Main Python application
├── random_paragraphs.txt  # Sample text file for analysis (8.26 MB)
└── README.md              # This file
```

## Installation

### Step 1: Clone or Download the Project

```bash
cd /home/hamza/Downloads/Dockerization-main
```

### Step 2: Build the Docker Image

```bash
docker build -t text-analysis-app .
```

This command will:
- Pull the Python 3.9 Alpine base image
- Copy the application files into the container
- Install NLTK library
- Download required NLTK data (stopwords and punkt tokenizer)

**Note**: The initial build may take a few minutes depending on your internet connection.

## Usage

### Run the Container

```bash
docker run text-analysis-app
```

The application will:
1. Read the `random_paragraphs.txt` file
2. Tokenize the text into words
3. Filter out English stop words
4. Count word frequencies
5. Display results in the format: `word <word> count is <number>`

### Alternative: Interactive Mode

To run the container interactively:

```bash
docker run -it text-analysis-app /bin/sh
```

This allows you to explore the container environment or run the script manually:

```bash
python python_app.py
```

## How It Works

### Application Workflow

1. **File Reading**: Opens `random_paragraphs.txt` and reads its contents
2. **Tokenization**: Uses NLTK's `word_tokenize()` to split text into words
3. **Filtering**: Removes non-alphabetic tokens and English stop words (e.g., "the", "is", "at")
4. **Word Counting**: Counts occurrences of each unique word using a custom function
5. **Output**: Prints word frequency pairs to console

### Code Breakdown

```python
# Read the text file
file = open("random_paragraphs.txt", mode="r")
filewords = file.read()

# Download NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

# Load English stop words
stop_words = set(stopwords.words('english'))

# Tokenize and filter
words = word_tokenize(filewords)
filtered_words = [word for word in words 
                  if word.isalpha() and word.lower() not in stop_words]

# Count word frequencies
uniquewords = list(set(filtered_words))
for w in uniquewords:
    count = count(w, filtered_words)
    print('word', w, 'count is', count)
```

## Docker Configuration

### Dockerfile Explained

```dockerfile
# Base image: Python 3.9 on Alpine Linux (lightweight)
FROM python:3.9-alpine

# Set working directory in container
WORKDIR /app

# Copy application files
COPY python_app.py /app/
COPY random_paragraphs.txt /app/

# Install NLTK library
RUN pip install nltk

# Download NLTK data packages
RUN python -m nltk.downloader stopwords punkt

# Run the application on container startup
CMD ["python", "python_app.py"]
```

### Why Alpine?

- **Minimal Size**: Alpine Linux images are ~5MB compared to ~900MB for standard Python images
- **Security**: Smaller attack surface with fewer installed packages
- **Performance**: Faster build and deployment times

## Output

Sample output format:

```
word computational count is 45
word technology count is 128
word analysis count is 67
word processing count is 92
...
```

The output shows each unique word (after filtering) and its frequency in the text.

## Customization

### Analyze Your Own Text File

1. Replace `random_paragraphs.txt` with your own text file
2. Update `python_app.py` line 1 to reference your filename:
   ```python
   file = open("your_filename.txt", mode="r")
   ```
3. Rebuild the Docker image

### Modify Stop Words

To use a different language's stop words:

```python
stop_words = set(stopwords.words('spanish'))  # or 'french', 'german', etc.
```

Available NLTK languages: Arabic, Azerbaijani, Danish, Dutch, English, Finnish, French, German, Greek, Hungarian, Indonesian, Italian, Kazakh, Nepali, Norwegian, Portuguese, Romanian, Russian, Slovenian, Spanish, Swedish, Tajik, Turkish

### Change Output Format

Modify the print statement in `python_app.py`:

```python
# CSV format
print(f"{key},{value}")

# JSON format
import json
print(json.dumps({key: value}))
```

## Troubleshooting

### Issue: Container Exits Immediately

**Solution**: Check container logs:
```bash
docker logs <container_id>
```

### Issue: NLTK Data Not Found

**Solution**: Ensure NLTK downloads complete during build:
```bash
docker build --no-cache -t text-analysis-app .
```

### Issue: File Not Found Error

**Solution**: Verify files are copied correctly in Dockerfile:
```dockerfile
COPY python_app.py /app/
COPY random_paragraphs.txt /app/
```

### Issue: Memory Limit Exceeded

For very large files, increase Docker memory allocation:
```bash
docker run -m 2g text-analysis-app
```

## Contributing

Contributions are welcome! Here are some ideas for improvement:

- Add command-line arguments for file selection
- Implement export to CSV/JSON
- Add graphical visualization of word frequencies
- Support multiple file formats (PDF, DOCX, HTML)
- Include sentiment analysis
- Add unit tests
- Create a web interface using Flask

---

**Built with Python | NLTK | Docker**
