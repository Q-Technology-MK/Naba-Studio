## AWS EC2 Django Deploy — Tam Rehber

Bu rehber, Nabastudio Django uygulamasını AWS EC2 üzerinde Ubuntu 22.04 ile üretime almanız için adım adım talimatları içerir.

---

### 1. EC2 Instance Oluşturma
1. AWS Console → **EC2** → **Launch Instance**
2. Ayarlar:
   - **Name**: `nabastudio-wedding`
   - **AMI**: Ubuntu Server 22.04 LTS
   - **Instance type**: `t2.micro` (Free tier) veya ihtiyaca göre `t2.small`
   - **Key pair**: Yeni oluşturun ve `.pem` dosyasını indirin
   - **Security Group**:
     | Type | Port | Source |
     |------|------|--------|
     | SSH  | 22   | Your IP |
     | HTTP | 80   | Anywhere |
     | HTTPS | 443 | Anywhere |
3. **Launch Instance** tıklayın.

---

### 2. EC2’ye Bağlanma
PowerShell veya Git Bash üzerinde:

```bash
ssh -i "YOUR_KEY.pem" ubuntu@YOUR_EC2_PUBLIC_IP
```

---

### 3. Sunucu Kurulumu (EC2’de)
```bash
# Sistem güncellemesi
sudo apt update && sudo apt upgrade -y

# Gerekli paketler
sudo apt install -y python3-pip python3-venv python3-dev nginx \
    postgresql postgresql-contrib libpq-dev

# Proje klasörü
sudo mkdir -p /var/www/nabastudio
sudo chown ubuntu:ubuntu /var/www/nabastudio
cd /var/www/nabastudio

# Repo klonla (kendi repo bilgilerinle değiştir)
git clone https://github.com/KULLANICI/REPO.git .

# Sanal ortam
python3 -m venv venv
source venv/bin/activate

# Bağımlılıklar
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn
```

---

### 4. PostgreSQL Kurulumu
```bash
sudo -u postgres psql
```
```sql
CREATE DATABASE nabastudio_db;
CREATE USER nabastudio_user WITH PASSWORD 'GÜÇLÜ_ŞİFRE';
ALTER ROLE nabastudio_user SET client_encoding TO 'utf8';
ALTER ROLE nabastudio_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE nabastudio_user SET timezone TO 'Europe/Istanbul';
GRANT ALL PRIVILEGES ON DATABASE nabastudio_db TO nabastudio_user;
GRANT ALL ON SCHEMA public TO nabastudio_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO nabastudio_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO nabastudio_user;
\q
```

---

### 5. Environment Dosyası
```bash
nano /var/www/nabastudio/.env
```

```env
SECRET_KEY=q@k*=pcpa%*t7xddo@+vyrrve$c!39%@&q&+a891bj===*d)o%
DEBUG=False
ALLOWED_HOSTS=nabastudiobysemma.com,www.nabastudiobysemma.com,YOUR_EC2_PUBLIC_IP
CSRF_TRUSTED_ORIGINS=https://nabastudiobysemma.com,https://www.nabastudiobysemma.com
DATABASE_URL=postgres://nabastudio_user:GÜÇLÜ_ŞİFRE@localhost:5432/nabastudio_db
```

> `.env` dosyası kaydedildikten sonra `EnvironmentFile` olarak Gunicorn servisinde kullanılacak.

---

### 6. Django Komutları
```bash
cd /var/www/nabastudio
source venv/bin/activate

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

---

### 7. Gunicorn Systemd Servisi
```bash
sudo nano /etc/systemd/system/gunicorn.service
```

```ini
[Unit]
Description=gunicorn daemon for nabastudio
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/var/www/nabastudio
EnvironmentFile=/var/www/nabastudio/.env
ExecStart=/var/www/nabastudio/venv/bin/gunicorn --access-logfile - \
  --workers 3 --bind unix:/var/www/nabastudio/gunicorn.sock \
  wedding_site.wsgi:application

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
sudo systemctl status gunicorn
```

---

### 8. Nginx Konfigürasyonu
```bash
sudo nano /etc/nginx/sites-available/nabastudio
```

```nginx
server {
    listen 80;
    server_name nabastudiobysemma.com www.nabastudiobysemma.com;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        alias /var/www/nabastudio/staticfiles/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/nabastudio/gunicorn.sock;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/nabastudio /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

---

### 9. SSL (Let’s Encrypt)
```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d nabastudiobysemma.com -d www.nabastudiobysemma.com
```

> DNS kayıtlarınız propagasyonunu tamamladıktan sonra çalıştırın. Yenileme Cron’u certbot tarafından otomatik eklenir.

---

### 10. DNS Ayarları
Alan adı sağlayıcınızda (Cloudflare / registrar):

| Type | Name | Value                | Proxy |
|------|------|----------------------|-------|
| A    | @    | YOUR_EC2_PUBLIC_IP   | DNS only |
| A    | www  | YOUR_EC2_PUBLIC_IP   | DNS only |

> Cloudflare kullanıyorsanız sertifika alma sürecinde **Proxy (turuncu bulut)** kapalı olmalı; SSL tamamlandıktan sonra tekrar açabilirsiniz.

---

### Son Kontroller
1. `https://nabastudiobysemma.com` adresini test edin.
2. Django admin girişini doğrulayın: `/admin/`
3. `sudo systemctl status gunicorn` ve `sudo systemctl status nginx` ile servislerin aktif olduğundan emin olun.
4. Gerekirse Cloudflare proxy’lerini yeniden etkinleştirin ve SSL mode’unu “Full (Strict)” yapın.

Hazırsınız! Uygulamanız artık AWS EC2 üzerinde güvenli şekilde çalışıyor.
