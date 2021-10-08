FROM python:3.7-alpine
ADD main.py .
#RUN pip install Counter socket os
RUN mkdir -p /home/data
RUN mkdir -p /home/output
ADD IF.txt ./home/data
RUN touch ./home/output/result.txt
ADD Limerick-1-1.txt ./home/data
CMD ["python", "./main.py"]