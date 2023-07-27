# Use the base image with Nvidia CUDA GPU support
FROM nvidia/cuda:11.6.2-cudnn8-devel-ubuntu20.04

# Install necessary dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Spacy with GPU support and Cupy
ADD requirements.txt .

RUN pip install -r requirements.txt

# Copy the Python script into the container
COPY app.py /app.py

# Set the working directory
WORKDIR /

# Expose the port used by the Flask app
EXPOSE 5000
EXPOSE 5501

# Run the Flask API
CMD ["python3", "/app.py"]