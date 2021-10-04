FROM python:latest

ADD IF.txt ./home/data

ADD Limerick-1-1.txt ./home/data

ADD main.py .

CMD ["python", "main.py"]