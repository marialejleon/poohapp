FROM python:3.8.5 
RUN pip3 install flask
COPY api.py .
CMD ["python3", "api.py"]