FROM python:3.9
EXPOSE 8501
COPY . /app
WORKDIR /app
RUN pip3 install -r ./dashboard/requirements.txt
CMD ["streamlit", "run", "./dashboard/app.py"]
# CMD ["ls"]