FROM python:3
RUN pip install flask
COPY . .
EXPOSE 8000
CMD ["python", "app.py"]
