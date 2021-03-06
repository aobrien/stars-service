# STARS Service 

**STARS COLLABORATE** is a C++ library for simulation of constellations of adaptive and collarborate satellite systems.  The library was orginally developed by Ryan Linnabary and distributed on GitHub [here](https://github.com/linnabary/collaborate).  A new version has been [forked](https://github.com/aobrien/stars-collaborate) and forms the basis for this service.  

The **STARS Service** is an HTTP-based RESTful web service that provides a simple way for users to run STARS COLLABORATE simulations.  The API provides functionality for long-running jobs, which are submitted, managed, and deleted.  Jobs produce simulation output data that can be downloaded and deleted through the service.  The code in this repo is divided into a server and client side.  The server side API implementation is in Python3 utilizing Flask & Connexion and running in a Docker container.  The client side test scripts for the API are provided as simple Python3 examples.  

The **STARS-Service API** is formally defined in Swagger YAML and can be explored online at [STARS-Service on SwaggerHub](https://app.swaggerhub.com/apis/aobrien/STARS-Service)

## JSON and the STARS-Service API

A STARS COLLABORATE simulation job is created by submitting a JSON-formatted simulation configuration. An example .json file is available [here](https://github.com/aobrien/stars-service/blob/master/json/example.json).  We are utilizing the official [JSON Schema](https://json-schema.org) for annotation and partial validation of simulation configurations.  The JSON schema is currently a DRAFT version and is still being revised as development continues, but please see the [JSON Format Wikipage](https://github.com/aobrien/stars-service/wiki/JSON-Format-for-STARS-Simulation-Configuration) for detailed information.

The STARS-Service API calls also use JSON formatted input and outputs, as described at the [STARS-Service on SwaggerHub](https://app.swaggerhub.com/apis/aobrien/STARS-Service).

## Using the STARS Service

### Setting up fresh Ubuntu Installation
If you are starting from a fresh Ubuntu 20.04 installation, the only requirements are git and docker:
```
sudo apt install git docker.io
```
After installing docker, you will likely want to run it as a non-root user.  You then need to get permission to access the Docker daemon socket ([more information](https://docs.docker.com/engine/install/linux-postinstall/)).  Run
```
sudo groupadd docker
sudo usermod -aG docker ${USER}
```
and then log out and back in again. Test docker using
```
docker run hello-world
```

### Downloading Prebuilt STARS Service Docker Image
The prebuilt STARS-Service Docker image is available on [DockerHub](https://hub.docker.com/r/aobrien200/stars-service).  An automatic build process updates the image as this repo is updated.  The image can be downloaded by running
```
docker pull aobrien200/stars-service:latest
```

### Building the STARS Service Docker Image
Alternatively, the image can be built from the source code in this repo.  First, clone this repo from GitHub:
```
git clone https://github.com/aobrien/stars-service.git
```
To build the stars-service image, run the following command in the root directory:
```
docker build --network="host" -t aobrien200/stars-service .
```
The image is currently based on Ubuntu 20.04, although future work will emphasize a more lightweight base.  

### Running STARS Service Container

Run the stars-service in a container using:
```
docker run -p 8080:8080 --network="host" \
       -v $(pwd)/workspace:/workspace \
       aobrien200/stars-service
```
or the shell script       
```
./docker_run_stars_service.sh
```
It is curently designed to use the host network via port 8080 (although this may change in the future). 

## Testing the STARS Service with a REST Client

A simple Python3 REST Client example program is provided to interface with the Webserve and exercise different functions, 
```
./client/test.py
```

Additionally, you can point a browser to 'http://localhost:8080/ui` to see the Swagger UI interface and explore the API.

---

*Authors: Andrew O'Brien & Ryan Linnabary, 2020*
