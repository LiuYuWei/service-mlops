## Docker configuration 

## Installation
Before you run the service, you need to build up the docker images.
```cmd
$ ./docker-initial-service.sh
$ ./docker-build-service.sh
```

## Running

### Start service
Execute the following command to start services:
```bash
$ ./docker-start-service.sh
```

### Stop service
Execute the following command to stop services:
```bash
$ ./docker-pause-services.sh
```

### Remove service
Execute the following command to stop and completely remove deployed docker containers:
```bash
$ ./docker-remove-services.sh
```
