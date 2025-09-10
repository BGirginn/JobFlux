from fastapi import HTTPException, Header, status

def get_current_user(authorization: str = Header(...)):
    # In a real application, you would decode and verify the JWT token here.
    # For now, we just check if a token is present.
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = authorization.split(" ")[1]
    # Simulate token verification
    if token == "valid-jwt-token":
        return {"username": "testuser"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
