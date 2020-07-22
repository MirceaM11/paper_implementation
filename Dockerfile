FROM python:3.8.4

COPY infinite-strategies-env /srv/pyCode/infinite-strategies-env
WORKDIR /srv/pyCode/infinite-strategies-env
COPY main.sh /bin/
RUN  chmod +x /bin/main.sh && pip install -r requirements.txt

ENTRYPOINT [ "/bin/main.sh" ]

# python3 /srv/pyCode/infinite-strategies-env/src/round_robin.py -m 10 -t 500
# /srv/pyCode/infinite-strategies-env/src/infinite_strategies/round_robin.py -m 10 -t 500