FROM python:3.10.2
WORKDIR /donutr COPY . /donutr
RUN pip install -r requirements.txt
 ENTRYPOINT ["bash"]
 CMD ["flask run"]
