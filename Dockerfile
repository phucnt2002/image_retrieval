# Use an official Python runtime as a parent image
FROM python:3.10.13-bullseye

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN pip install --no-cache-dir -r requirements.txt
RUN python -c "from keras.applications.vgg16 import VGG16; VGG16()"

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Create directories for static datasets
# RUN mkdir -p ./static/datasets/oxbuild/images
# RUN mkdir -p ./static/datasets/paris/images

# Copy dataset images into the respective directories
# Copy dataset images into the respective directories
# COPY ./static/datasets/oxbuild/images /app/static/datasets/oxbuild/images
# COPY ./static/datasets/oxbuild/images /app/static/datasets/paris/images

# Set environment variables
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Run app.py when the container launches
CMD ["flask", "run", "-h","0.0.0.0"]
# FROM image_retrievel:v3
# # Set the working directory in the container to /app
# WORKDIR /app

# # Add the current directory contents into the container at /app
# ADD . /app