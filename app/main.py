import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from app.api.v1.api import router as api_router

###############################################################################
#   Application object                                                        #
###############################################################################
app = FastAPI()

###############################################################################
#   Routers configuration                                                     #
###############################################################################
@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(api_router, prefix="/api/v1")

###############################################################################
#   Handler for AWS Lambda                                                    #
###############################################################################
handler = Mangum(app)

###############################################################################
#   Run the self contained application                                        #
###############################################################################
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)