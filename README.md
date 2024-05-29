# Composer for NucleUS

## Clone
Clone the repository with the submodules:

```
git clone --recursive git@github.com:NucleUS-EGS/composer.git
```

## IDP Proxy

Because the Client credentials given to us for the Universidade de Aveiro's IDP only work on localhost, we need to use a server proxy running locally to handle the data from the IDP login and redirect it to the server (proof of concept purposes only).

### Setup

1. Make a Python virtual environment (optional):
```bash
cd idp_proxy

python3 -m venv venv
source venv/bin/activate
```

2. Install the requirements:
```bash
pip install -r requirements.txt
```

3. Create .env file with the following content:
```bash
FLASK_RUN_PORT=5000 # Must match the redirect URI port
FLASK_RUN_HOST="0.0.0.0"

IDP_REDIRECT_URI = "http://localhost:5000" # One of the enforced redirect URIs
IDP_BASE_URL = "https://wso2-gw.ua.pt"
CLIENT_ID = <CLIENT_ID>
CLIENT_SECRET = <CLIENT_SECRET>

# APP_REDIRECT_URI = "http://localhost:8080/auth/v1/idp"
APP_REDIRECT_URI = "http://http://grupo5-egs-deti.ua.pt/auth/v1/idp"
```


4. Run the proxy:
```bash
flask run
```

## Docker

```
docker-compose up --build
```

## Kubernetes

### Build and push images

For each service (auth, events, nginx, points and webapp), build the image and push it to the registry.

```bash
./service.sh <image_name> <version>
```

or

```bash
docker buildx build --platform linux/amd64 --network=host -t registry.deti/egs-nucleus/<image_name>:<version> -f <image_name>.dockerfile .
docker push registry.deti/egs-nucleus/<image_name>:<version>
```

### Deploy

```bash
kubectl apply -f storage.yaml
kubectl apply -f deployment.yaml
```

### Delete

```
kubectl delete -f deployment.yaml
kubectl delete -f storage.yaml
```