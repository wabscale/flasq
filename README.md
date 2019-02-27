[![pipeline status](https://gitlab.com/b1g_J/flasq/badges/master/pipeline.svg)](https://gitlab.com/b1g_J/flasq/commits/master)

# flasq
For when you need a quick flask app, but are too lazy to write the basics.

# Quickstart

### Project structure
Flasq was made in a way that intends you to follow a specific structure for defining routes. Each route should get its own folder with a couple of default files. The structure should be about the following:

```
routename
├──  forms.py     # where you can define your flask forms
├──  __init__.py  # one line importing blueprint object from routes.py
├──  models.py    # where you can define your database models
└──  routes.py    # where you define your blueprint and its routes
```

Obviously you can do whatever you want, but I would recomend following that structure. It may be easiest to refer back to the auth folder to see how things are structured there when writing new sections.

### Debuging
Debuging is easy! Just run `make run`. the first time you run this, it will create a `virtualenv` with all the dependencies you need. To clean your project of all these files just run `make clean`. If you want to test the docker container, you can do that with `make build && make rund`. This will build the container, then run it. If you need to change the docker options, feel free to edit the `Makefile`. There is a convinient variable called `DOCKER_OPTIONS` that is defined at the top. Anything you put there will be an option when the container is run.

### Deploying
When you deploy your flasq app, there are two folders that will be mounted to your docker container (If you use my `docker-compose.yml`). To deploy all you need to do is run the deploy target:

```
make deploy
```

### traefik
You will want to read up on how traefik works, as it is how the container will get routed too. Make sure to add your trafik labels in the `docker-compose.yml` and update the acme and docker info in `traefik.toml`.


# Maintainer
- big_J
