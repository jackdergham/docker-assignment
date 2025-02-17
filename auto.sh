#! /usr/bin/bash

# Function to check if Docker images are already built
check_images() {
    docker images | grep 'producer' > /dev/null && docker images | grep 'consumer' > /dev/null
}

# Stop and remove existing containers
echo "Stopping and removing existing containers..."
docker compose down --volumes

# Check if images exist
if check_images; then
    echo "Images already exist. Starting containers without rebuilding..."
    docker compose up --no-build
else
    echo "Building Docker images and starting containers..."
    docker compose up --build
fi