from fastapi import APIRouter
from config.database import Database

router = APIRouter() # APIRouter instance to handle routing related to a particular resource
db = Database()  # Create an instance of the Database class to interact with the database

# Define a GET route for the health check endpoint
@router.get("/")
def health_check():
    # Check if the database connection is successful
    if db.check_connection():
        return {"status": "OK"}

    # If the connection fails, return a status of "ERROR"
    return {"status": "ERROR"}
