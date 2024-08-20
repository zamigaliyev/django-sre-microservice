FROM python:3.9
WORKDIR /app
COPY myproject /app
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
