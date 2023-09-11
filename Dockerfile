FROM python:3.9
WORKDIR /code
EXPOSE 8888
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./notebooks /code

CMD ["jupyter-lab", "--config=.\jupyter_lab_config.py"]