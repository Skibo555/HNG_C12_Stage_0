from fastapi import FastAPI, Depends, HTTPException, Response, status
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import uvicorn


app = FastAPI()

# Define allowed origins
origins = [
    "*",  # Allows all domains
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get('/', status_code=status.HTTP_200_OK)
def index():
    # Get current date and time
    now = datetime.now()
    my_email = "yonwatodejulius@gmail.com"
    github_url = "https://github.com/Skibo555"

    # Format the date in ISO 8601 format
    iso_timestamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    res = {
        "email": my_email,
        "current_datetime": iso_timestamp,
        "github_url": github_url
    }

    return res


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
