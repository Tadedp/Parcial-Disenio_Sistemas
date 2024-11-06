import uvicorn
from fastapi import FastAPI
from starlette import status
from starlette.responses import JSONResponse

from config.database import Database
from controllers.adn_controller import ADNController
from controllers.health_check import router as health_check_controller
from repositories.base_repository_impl import InstanceNotFoundError

# Create and configure the FastAPI application
def create_fastapi_app():
    fastapi_app = FastAPI()

    @fastapi_app.exception_handler(InstanceNotFoundError)
    async def instance_not_found_exception_handler(request, exc):
        # Return a 404 Not Found JSON response if the instance is not found
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": str(exc)},
        )

    # ADN controller for handling /mutant routes
    client_controller = ADNController()
    
    # Include the ADN controller router with the "/mutant" prefix
    fastapi_app.include_router(client_controller.router, prefix="/mutant")

    # Include the health check router with the "/health_check" prefix
    fastapi_app.include_router(health_check_controller, prefix="/health_check")

    # Return the configured FastAPI application
    return fastapi_app

# Run FastAPI app using Uvicorn on host 0.0.0.0 and port 8000
def run_app(fastapi_app: FastAPI):
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    # Initialize the database and create necessary tables
    db = Database()
    db.create_tables()
    app = create_fastapi_app()
    run_app(app)