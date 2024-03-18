# fast-api

Run app: `gunicorn -w 4 -k uvicorn.workers.UvicornWorker --preload main:app`

1. **Use Uvicorn as the Worker Class:** Gunicorn works best with FastAPI when using Uvicorn as the worker class. Uvicorn is an ASGI server implementation and is well-suited for running asynchronous web applications. Specify Uvicorn as the worker class with the -k option. This command starts Gunicorn with 4 worker processes (-w 4) and uses Uvicorn as the worker class.
1. **Enable Preloading:** To allow Gunicorn to manage the number of worker processes dynamically, you can enable preloading of the application code with the --preload option. This ensures that the application code is loaded into memory before forking worker processes. With preloading enabled, Gunicorn can dynamically adjust the number of worker processes based on the server load.