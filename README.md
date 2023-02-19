# Screenshare-back

## 🧐 Project structure

    ├── devops                   # Containd dockerfiles for develop and production
    │ ├── dev                    # Development environment
    │ └── prod                   # Production Dockerfile and docker-compose
    ├── Makefile                 # Used to build, connect to container, format code etc
    ├── README.md
    └── src                      # Cointains the code of the aplication

## 🚀 Makefile usage

Makefile variables that can be customized:

| Variable |     Default      |
|----------|:----------------:|
| DOCKER_IMAGE_NAME | screenshare-back |
| PROD_TAG|      0.0.1       |

* Build docker image for development
    ```
    make dev/build
    ```

* Run development docker
    ```
    make dev/shell
    ```
* Format code using black
    ```
    make black
    ```

