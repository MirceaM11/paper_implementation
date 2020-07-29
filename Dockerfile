FROM python:3.8.4

COPY infinite-strategies-env /srv/pyCode/infinite-strategies-env
WORKDIR /srv/pyCode/infinite-strategies-env
COPY main.sh /bin/
RUN  chmod +x /bin/main.sh && pip install -r requirements.txt

ENTRYPOINT [ "/bin/main.sh", "10" ]
