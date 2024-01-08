# python-docker-yoda-cowsay
### App Name: Cowsay Tux

***Description:***
### Cowsay Tux is a simple Python application that uses various tools such as cowsay, ponysay, and tuxsay to generate colorful and fun messages on the terminal. Additionally, the application uses Dockerfile to build two versions of the Docker image: full and minimal, which are stored on Docker Hub.
![cowsay](ansible/src/image1.png)
***Directory structure:***

     app: Directory containing the application's source files.

         tux.py: A Python script that generates messages and uses tuxsay.
         cowsay.sh: A bash script that uses cowsay to generate messages.
         requirements.txt: File containing Python dependencies.
         yoda.txt: File with sample ASCII art of Yoda.

     Dockerfile: The Dockerfile used to build a Docker image.

***Instructions:***

     In the app directory you will find application scripts and source files.
     tux.py generates colored messages using tuxsay.
     cowsay.sh uses cowsay to generate messages.
     To run the application locally, use the scripts in the app directory.
     The requirements.txt file contains Python dependencies. Install them with pip install -r requirements.txt.
     The Dockerfile allows you to build two versions of the Docker image: full and minimal.

***Docker Build Instructions:***

     Run docker build -t image_name:tag -f Dockerfile . in the root directory to build the image.
     Build both images using the full and small tags.

***Docker Image Versions:***

     image_name:full: Full version with all tools.
     image_name:small: Minimal version with limited tools.

### Yoda ASCII Art:
***View the yoda.txt file in the app directory for an example of ASCII Art Yoda.***

![cowsay](ansible/src/image.png)