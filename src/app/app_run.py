#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from src.app import create_app

app = create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=8080, threaded=True)
