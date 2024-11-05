import uvicorn
from fastapi import FastAPI
from starlette import status
from starlette.responses import JSONResponse

from config.database import Database
from controllers.adn_controller import ADNController
from controllers.health_check import router as health_check_controller
from repositories.base_repository_impl import InstanceNotFoundError

def create_fastapi_app():
    fastapi_app = FastAPI()

    @fastapi_app.exception_handler(InstanceNotFoundError)
    async def instance_not_found_exception_handler(request, exc):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": str(exc)},
        )

    client_controller = ADNController()
    fastapi_app.include_router(client_controller.router, prefix="/mutant")

    fastapi_app.include_router(health_check_controller, prefix="/health_check")

    return fastapi_app

def run_app(fastapi_app: FastAPI):
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    db = Database()
    db.drop_database()
    db.create_tables()
    app = create_fastapi_app()
    run_app(app)