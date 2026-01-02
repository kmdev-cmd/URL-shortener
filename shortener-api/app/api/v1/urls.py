from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import secrets
import string

from ...database import get_db
from ...models.url import Url
from ...schemas.url import UrlCreate, UrlResponse
from ...dependencies.auth import get_current_user
from ...core.config import settings

router = APIRouter()

def generate_short_code(length: int = 6) -> str:
    """Gera um código curto aleatório"""
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))

@router.post("/", response_model=UrlResponse)
def create_url(
    url_in: UrlCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    # Verifica se o código personalizado já existe
    if url_in.custom_code:
        existing_url = db.query(Url).filter(Url.short_code == url_in.custom_code).first()
        if existing_url:
            raise HTTPException(
                status_code=400,
                detail="Código personalizado já está em uso"
            )
        short_code = url_in.custom_code
    else:
        # Gera código único
        short_code = generate_short_code()
        while db.query(Url).filter(Url.short_code == short_code).first():
            short_code = generate_short_code()

    # Cria a URL
    new_url = Url(
        original_url=str(url_in.original_url),
        short_code=short_code,
        owner_id=current_user.id
    )
    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    # Retorna resposta com URL completa
    return UrlResponse(
        id=new_url.id,
        original_url=new_url.original_url,
        short_code=new_url.short_code,
        short_url=f"{settings.BASE_URL}/{new_url.short_code}",
        clicks=new_url.clicks,
        created_at=new_url.created_at
    )

@router.get("/", response_model=List[UrlResponse])
def get_user_urls(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    urls = db.query(Url).filter(Url.owner_id == current_user.id).all()
    return [
        UrlResponse(
            id=url.id,
            original_url=url.original_url,
            short_code=url.short_code,
            short_url=f"{settings.BASE_URL}/{url.short_code}",
            clicks=url.clicks,
            created_at=url.created_at
        )
        for url in urls
    ]

@router.delete("/{url_id}")
def delete_url(
    url_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    url = db.query(Url).filter(Url.id == url_id, Url.owner_id == current_user.id).first()
    if not url:
        raise HTTPException(status_code=404, detail="URL não encontrada")

    db.delete(url)
    db.commit()
    return {"message": "URL deletada com sucesso"}
