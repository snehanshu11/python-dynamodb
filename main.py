
from fastapi import FastAPI,status, HTTPException
from logic import create_post,query_by_user_id
from models import UserPost

app = FastAPI()



@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_one_post(post:UserPost):
    my_post= create_post(post.model_dump())
    if not my_post:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"")
    return {"msg": "post created successfully", "data": my_post}


@app.get("/users/{id}")
async def get_post(id:str):
    post = query_by_user_id(id)
    return post["Items"]