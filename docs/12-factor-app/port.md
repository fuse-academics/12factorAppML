## 7. Services via Port binding

> **Export services via port binding**

1. The twelve-factor app is completely self-contained and does not rely on runtime injection of a webserver into the execution environment to create a web-facing service. 
2. The web app exports HTTP as a service by binding to a port, and listening to requests coming in on that port. 

**In most languages this is done by using a webserver library.** 

- HTTP is not the only service that can be exported by port binding. 
- Nearly any kind of server software can be run via a process binding to a port and awaiting incoming requests. 

*Examples include ejabberd (speaking XMPP), and Redis (speaking the Redis protocol).*


### FastAPI

[FastAPI Documentation](https://fastapi.tiangolo.com/)
```bash
pip install fastapi

pip install uvicorn
```
```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```
To run a fastapi application *Specify HOST 0.0.0.0 and Port 8000* using `environment variables`
```bash
uvicorn app.main:app --host ${HOST} --port ${PORT}
```


<details>
<summary>Flask</summary>

[Flask](https://flask.palletsprojects.com/en/3.0.x/)
</details>

<details>
<summary>Tornado</summary>

[Tonado](https://www.tornadoweb.org/en/stable/)
</details>
