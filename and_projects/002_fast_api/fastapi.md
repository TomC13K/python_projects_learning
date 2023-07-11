# installation

install the package, including uvicorn server
```bash
pip install "fastapi[all]"

```


# run - non dockerized version
- new with app folder and main.py
```bash
python3 main.py
```


- old before app folder
```bash
uvicorn main:app --reload
```
# DOCKER stuff
- have colima installed on mac - its the container engine
```bash
brew install docker docker-compose
brew install colima
```

## Colima commands
```bash
# start the docker engine
colima start

# shows status
colima status

# stop
colima stop

# set runtime with containerd engine - not a docker
colima start --runtime containerd

# delete existing colima instance
colima delete
# then start again
colima start

#edit config
colima start --edit
```

- start colima so we can use docker commands
```bash
colima start
```

- when dockerfile is available, build & name the container with the app
```bash 
docker build -t my-fastapi-app .
```
- then start the container with given  port & name 
```bash
docker run -it -p 8000:8000 my-fastapi-app
```
### Docker commands
```bash
# list running containers
docker images

# connect to a docker container and start bash
docker exec -it [container-id] bash

# show all the docker containers running on local
docker ps -aq

# shows stopped containers
docker ps -a

# stop all containers that are running
docker stop $(docker ps -aq)

# remove all containers that are stopped
docker rm $(docker ps -aq)
```


# path decorators
- @app.post()
- @app.put()
- @app.delete()
- @app.options()
- @app.head()
- @app.patch()
- @app.trace()

# tips
- path operations are evaluated in order, you need to make sure that the path for `/users/me` is declared before the one for `/users/{user_id}`
## generate requirements file
```bash
pip freeze > requirements.txt
```
