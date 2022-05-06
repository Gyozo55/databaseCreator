FROM mhoush/psycopg2

WORKDIR /app

COPY ./feladat.py ./

CMD [ "python3", "./feladat.py"]
