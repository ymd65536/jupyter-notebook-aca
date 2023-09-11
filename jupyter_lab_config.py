# Configuration file for lab.
# jupyter-lab --config=".\jupyter_lab_config.py"
import os

root_dir = os.getcwd()

c = get_config()  #noqa
c.LabApp.default_url = '/lab'
c.LabApp.port = 8888

c.ServerApp.ip = "0.0.0.0"
c.ServerApp.root_dir = f'{root_dir}\\notebooks'
