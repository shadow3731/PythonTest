import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


def mount_static(app: FastAPI):
    static_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..',
        'static',
    )
    app.mount(
        '/static', 
        StaticFiles(directory=static_dir), 
        name='static',
    )