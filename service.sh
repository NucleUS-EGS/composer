#!/bin/bash

# Load registry configuration
if [ ! -f registry.conf ]; then
	echo "registry.conf not found"
	exit 1
fi
source registry.conf

# Load arguments
if [ "$#" -ne 2 ]; then
	echo "Usage: $0 <image_name> <version>"
	exit 1
fi
IMAGE_NAME=$1
VERSION=$2

SERVICE="${REGISTRY_URL}/${NAMESPACE}/${IMAGE_NAME}:${VERSION}"

# Build and push image
docker buildx build --platform linux/amd64 --network=host -t ${SERVICE} -f ${IMAGE_NAME}.dockerfile .
docker push ${SERVICE}
