[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=dead_baha_31
Group=www-data
WorkingDirectory=/home/dead_baha_31/hackathon_04
ExecStart=/home/dead_baha_31/hackathon_04/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/dead_baha_31/hackathon_04/hackathon.sock main.wsgi:application

[Install]
WantedBy=multi-user.target