from pydantic import BaseModel,HttpUrl

class Website(BaseModel):
    url: HttpUrl
