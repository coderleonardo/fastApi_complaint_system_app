import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="localhost",
        port=9696,
        log_level="info",
        reload=True
    )