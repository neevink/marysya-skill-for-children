# Скилл маруси для детей

## Деплой

Чтобы подключиться к виртуальной машине, введите в консоль:
```shell
ssh -i "marusya-skill.pem" ubuntu@ec2-13-59-178-53.us-east-2.compute.amazonaws.com
```

Чтобы установить `nginx` на машину, введите в консоль:
```shell
sudo apt update
sudo apt install -y nginx
```

Перейти в настройки `nginx`:
```shell
sudo nano /etc/nginx/nginx.conf
```

