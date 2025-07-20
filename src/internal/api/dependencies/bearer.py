from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from src.config import settings

oauth2_scheme = HTTPBearer()  # use token authentication

def api_key_auth(api_key=Depends(oauth2_scheme)):
    api_keys = [settings.API_SECRET_KEY]
    if api_key.credentials not in api_keys:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization Failed")
