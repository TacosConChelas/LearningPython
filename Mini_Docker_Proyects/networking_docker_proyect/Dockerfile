FROM python:3.9-slim
WORKDIR /app
COPY webserver.py .

# OJO: EXPOSE es solo documentación. No abre el puerto realmente.
# Le dice al humano: "Oye, este programa usa el 8000".
EXPOSE 8000

CMD ["python", "webserver.py"]