from pydantic import BaseModel
class UserPost(BaseModel):
    user_id: str
    user_name:  str
    post_id: str
    title: str
    details: str