# Use a python 3.10 base image (on top of slim debian bullseye).
FROM python:3.10-slim-bullseye

# Set the working directory within the container's filesystem.
WORKDIR /app

# Copy the requirements.txt from our repository directory (where we build the docker image using this file).
COPY requirements.txt requirements.txt
# Install the requirements with pip within the container.
RUN pip3 install -r requirements.txt

# Copy all of our other files into the container's working directory.
# NOTE: Couldn't we just do this above instead of only copying over the requirements.txt file first?
# ALSO NOTE: We also created a docker ignore file to exclude copying files and folders that are totally irrelevant.
COPY . .

# Install ffmpeg.
RUN apt update && apt install ffmpeg -y


# Okay, everything above is what we've done to create the image. Docker build is basically looking at what we have
# so far and setting up a little linux environment. Once everything is set up in that little "Ubuntu install", we
# get an image. Think of this just like a virtual machine image as a mental model.

# So, we've specified above how to set up the linux environment we want to run our program in. NOW, all that's left
# to do is to actually specify what we want to happen every time we spin up our image! I.e., every time we run it,
# what do we want to run/be executed inside it? We define this below with the CMD. There is only ever one CMD in a
# docker file. You specify the commands you'd like to be run, along with any parameters.

CMD ["python3", "ratbot.py"]