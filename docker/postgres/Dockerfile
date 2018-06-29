FROM postgres:alpine

ENV BINSPDT_USER=binspdt \
    BINSPDT_PASSWORD=binspdt

COPY ./init-binspdt-db.sh /docker-entrypoint-initdb.d/init-binspdt-db.sh

ENTRYPOINT ["docker-entrypoint.sh"]
EXPOSE 5432
CMD ["postgres"]
