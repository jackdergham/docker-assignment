## Project Setup

### Requirements

- Make sure Docker and Docker Compose are properly installed on your machine.

- Clone this repository on your machine.

### Instructions

1. Automatic approach through the shell script

    Open a terminal in the directory where you cloned the repository and run the following command: `./auto.sh` .

2. Manual approach

    Open a terminal in the directory where you cloned the repository and run the command: `docker compose up --build`.

    This will automatically build the images and start up the containers directly in the terminal. `--build` can be ommited if the images have been built previously.

### Troubleshoot

- `docker ps` to check running containers.
- `docker exec -it <container name> sh` to open an interactive shell inside the desired container. If inside the consumer navigate to the data directory through `cd ../data/` and run `cat received_data.txt` to check the stored transmitted data from producer to consumer.