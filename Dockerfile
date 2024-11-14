FROM python:3
RUN pip install flask
COPY . .
CMD ["python",app.py"]
