FROM praekeltfoundation/python-base

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD /usr/local/bin/python -u rapidpro_to_bigquery.py
