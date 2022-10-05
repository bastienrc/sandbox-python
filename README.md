# Sandbox Python

Mise en place d'un environement de developpement avec docker.

TODO: Trouver comment faire fonctionner le devcontainer pour coder dedans

## Construction de l'image

```sh
docker build -t app .devcontainer
```

## Lancement

```sh
docker run -u=$(id -u $USER):$(id -g $USER) \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  -v $(pwd)/src:/app \
  --rm \
  -it \
  app \
  /bin/bash
```

## Dans le container, je lance mon script sans probleme

```sh
I have no name!@8d9cbfe12b16:/$ python app/main.py
```
