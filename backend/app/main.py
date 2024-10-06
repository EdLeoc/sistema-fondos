from fastapi import FastAPI
from app.routes.routes import router as fund_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8080",  # Permite solicitudes desde el frontend
]

# Middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(fund_router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Fondos de BTG"}
