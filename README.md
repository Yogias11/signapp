# signapp
Sign Approval Application for guidance and conseling Lecturer

## Requirement
 * virtualenv
 * uwsgi

### Instalation
```sh
# sudo apt-get install build-essential libssl-dev libffi-dev python-pip python-dev nginx
# pip install paramiko
# pip install virtualenv
# pip install uwsgi
```

### Setup
#### Direktory

```sh
$ mkdir signapp
$ cd signapp
$ virtualenv signappenv
$ source signappenv/bin/activate
$ deactivate
```

#### uwsgi

Please edit first signapp .ini and .conf; after that please copy .conf to your startup init

```sh
$ sudo cp signapp.conf /etc/init/
$ sudo start signapp
```

#### nginx

```sh
server {
    listen 80;
    server_name gitar.vas.web.id;

    location / {
        include         uwsgi_params;
        uwsgi_pass      unix:/home/devops/gitar/gitar.sock;
    }
}
```
