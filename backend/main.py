from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from actions.add_user import add_user
from actions.list_users import list_users
from actions.update_user import update_email
from actions.delete_user import delete_user
from db.db_setup import setup_database
from pydantic import BaseModel

# Inicializa o app FastAPI
app = FastAPI()
setup_database()  # Cria o banco ao iniciar, se necessário

# Libera CORS para acesso do Angular
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # ajuste se for usar online
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos Pydantic para validação dos dados recebidos
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class EmailUpdate(BaseModel):
    new_email: str

# Rotas da API
@app.get("/users")
def get_users():
    return list_users()

@app.post("/users")
def create_user(user: UserCreate):
    response = add_user(user.name, user.email, user.password)
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return response

@app.put("/users/{user_id}")
def update_user_email(user_id: int, data: EmailUpdate):
    response = update_email(user_id, data.new_email)
    if "error" in response:
        raise HTTPException(status_code=404, detail=response["error"])
    return response

@app.delete("/users/{user_id}")
def delete_user_by_id(user_id: int):
    response = delete_user(user_id)
    if "error" in response:
        raise HTTPException(status_code=404, detail=response["error"])
    return response
