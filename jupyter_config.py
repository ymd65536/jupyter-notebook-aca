# Configuration file for lab.

root_dir = '/home/jovyan/'
# 17fdfbeafa171980754c9ec1917436998c7410ae777ee85a
c.ServerApp.token = '17fdfbeafa171980754c9ec1917436998c7410ae777ee85a'
c.ServerApp.port = 8888
c.ServerApp.open_browser = False
c.ServerApp.allow_remote_access = True
c.ServerApp.allow_origin = '*'
c.ServerApp.ip='0.0.0.0'
c.ServerApp.notebook_dir = root_dir
c.ServerApp.allow_root = True

# docker build -t jupyter-nb . --no-cache
# docker run -it jupyter-nb bash
# docker run -itd -p 8888:8888 jupyter-nb
