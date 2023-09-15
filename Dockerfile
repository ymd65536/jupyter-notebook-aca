FROM jupyter/base-notebook:python-3.11
COPY jupyter_config.py /etc/jupyter/jupyter_server_config.py
EXPOSE 8888
