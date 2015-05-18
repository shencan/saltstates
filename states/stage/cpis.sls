httpd:
  pkg.installed

/etc/httpd/conf/httpd.conf:
  file.managed:
     - source: salt://httpd.conf
     - mode: 644
     - user: root
     - group: root
     - template: jinja
     - backup: minion
     - require:
        - pkg: httpd
/var/www/html/index.html:
  file.managed:
      - source: salt://index.html
apache:
   service.running:
      - name: httpd
      - require: 
        - pkg: httpd
      - watch:
        - file: /etc/httpd/conf/httpd.conf
