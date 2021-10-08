FROM python:3.7-alpine
ADD main.py .
#RUN pip install Counter socket os
RUN mkdir -p /home/data
ADD IF.txt ./home/data
ADD Limerick-1-1.txt ./home/data
CMD ["python", "./main.py"]