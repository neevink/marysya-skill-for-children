# Скилл маруси для детей

## Деплой

Чтобы подключиться к виртуальной машине, введите в консоль:
```shell
sudo ssh -i ./key.pem ubuntu@ec2-18-219-147-206.us-east-2.compute.amazonaws.com
```

Чтобы установить `nginx`, введите в консоль:
```shell
sudo apt update
sudo apt install -y nginx
```

Перейти в настройки `nginx`:
```shell
sudo nano /etc/nginx/nginx.conf
```

