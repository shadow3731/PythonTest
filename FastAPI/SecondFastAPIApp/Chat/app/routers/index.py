from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get('/', response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse(
        'index.html', 
        {
            'request': request,
            'online_amount': 0,
            'registered_amount': 0,
        }
    )