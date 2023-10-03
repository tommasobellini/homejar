FROM python:3.11-alpine
WORKDIR /home_jar_api
ENV PYTHONPATH ${PYTHONPATH}:/home_jar_api
COPY common_requirements.txt common_requirements.txt
COPY /app/requirements.txt /application/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . .
CMD ["uvicorn", "application.main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]