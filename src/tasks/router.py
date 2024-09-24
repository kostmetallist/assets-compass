from fastapi import APIRouter, Depends

from src.auth.base_config import current_user
from .tasks import generate_digest

router = APIRouter(prefix='/report')


@router.get('/digest')
def get_digest(user=Depends(current_user)):
    generate_digest.delay(user.username)
    return {
        'status': 200,
        'data': 'A digest was successfully been created',
        'details': None,
    }
