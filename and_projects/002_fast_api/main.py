import uvicorn


if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)

# need specify the host 0.0.0.0 for a docker container so it is accessible from everywhere not just localhost
