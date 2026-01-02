from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from ...database import get_db
from ...models.url import Url

router = APIRouter()

@router.get("/{short_code}")
def redirect_to_url(short_code: str, db: Session = Depends(get_db)):
    # Busca a URL pelo código curto
    url = db.query(Url).filter(Url.short_code == short_code).first()

    if not url:
        raise HTTPException(status_code=404, detail="URL não encontrada")

    # Incrementa contador de cliques
    url.clicks += 1
    db.commit()

    # Redireciona para a URL original
    return RedirectResponse(url.original_url)
