## 8. Concurrency

> **Scale out via the process model**

Any program in execution is represented by one more process. Tweleve-factor app take inspiration from unix **process model** for running service demons, where developer can architect the acpp to handle diverse workload by assigning each type of work to a process type. Eg.  HTTP requests may be handled by a web process, and long-running background tasks handled by a worker process.

- Rather than building one big monolithic service that does everything, you split your app into process types, each handling a specific kind of work.


![Process-types](https://12factor.net/images/process-types.png)

```bash
gunicorn --workers 4 --bind 0.0.0.0:5000 app.main:app
```

### Asyncio


[GeeksforGeeks](https://www.geeksforgeeks.org/asyncio-in-python/)

`pip install asyncio`
```python
import asyncio


async def func1():
    print("Function 1 started..")
    await asyncio.sleep(2)
    print("Function 1 Ended")


async def func2():
    print("Function 2 started..")
    await asyncio.sleep(3)
    print("Function 2 Ended")


async def func3():
    print("Function 3 started..")
    await asyncio.sleep(1)
    print("Function 3 Ended")


async def main():
    L = await asyncio.gather(
        func1(),
        func2(),
        func3(),
    )
    print("Main Ended..")


asyncio.run(main())
```
![Output](https://media.geeksforgeeks.org/wp-content/uploads/20230819125632/Output.jpg)

- [Twisted](https://twisted.org/) is an event-driven networking engine
