# signapp
Sign Approval Application for guidance and conseling Lecturer

## Requirement
 * virtualenv
 * uwsgi

### Instalation
Centos 6 x86_64_ (still on progress)
```sh
# yum --enablerepo=extras install centos-release-SCL
# yum install python27
# cd /etc/yum.repos.d/ 
# wget https://copr.fedorainfracloud.org/coprs/pypa/pypa/repo/epel-6/pypa-pypa-epel-6.repo
# yum clean all
# yum install python-backports
# rpm -ivh ftp://rpmfind.net/linux/centos/6.8/os/x86_64/Packages/python-backports-ssl_match_hostname-3.4.0.2-2.el6.noarch.rpm
# yum install python-pip
# pip install virtualenv
# pip install uwsgi
```

Centos 7
```sh
# yum install python-pip python-dev nginx
# pip install virtualenv
# pip install uwsgi
```


Ubuntu Installation
```sh
# sudo apt-get install build-essential libssl-dev libffi-dev python-pip python-dev nginx
# pip install virtualenv
# pip install uwsgi
```

### Setup
#### Direktory

```sh
$ cd signapp
$ virtualenv signappenv
$ source signappenv/bin/activate
$ deactivate
```

#### uwsgi
Please edit first signapp .ini

Centos 7
edit uwsgi.service; and copy to your centos 7 service dir

```sh
# cp uwsgi.service /etc/systemd/system/
# systemctl start uwsgi
# systemctl status uwsgi
# systemctl enable uwsgi
```


Ubuntu
edit signapp.conf; after that please copy .conf to your startup init

```sh
$ sudo cp signapp.conf /etc/init/
$ sudo start signapp
```

#### nginx

```sh
server {
    listen 80;
    server_name sign.vas.web.id;

    location / {
        include         uwsgi_params;
        uwsgi_pass      unix:/home/signapp/www/signapp.sock;
    }
}
```
