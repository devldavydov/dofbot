# Depth Of Field Telegram Bot
Bot for calculation Depth Of Field by focal length, aperture and focus distance for Full Frame cameras

## clone
```
git clone git@github.com:devldavydov/dofbot.git
```

## install
```
cd dofbot
pip install .
```

## run
```
dofbot telegram_api_token
dofbot -h
```

## run in Docker
```
cd dofbot
./docker_build.sh
docker run -d --restart always dofbot
```
