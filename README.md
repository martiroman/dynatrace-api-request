# dynatrace-billing

## Configuracion

> vim /etc/dynatrace-integrations/config.json

```json
{
    "DYNATRACE": {
        "API_URL" : "http://xxx.dynatrace.xxx",
        "API_TOKEN" : "xxxxxxxxxxxxxxxxxx"
    }
}
```

## Configuracion Apache:

* Instalar mod_wsgi
* Configurar apache. Ejemplo:

> sudo vi /etc/httpd/conf.d/python-wsgi.conf

```
WSGIScriptAlias /dynatrace /var/www/html/dynatrace/app.py

ErrorLog /var/log/httpd/dyna-error.log
CustomLog /var/log/dyna-access.log combined


<Directory "/var/www/html/dynatrace/">
   Order allow,deny
   Allow from all
</Directory>
```

> systemctl restart httpd