## 4. Backing Services

> Treat backing services as attached resources

A backing service is any service the app consumes over the network as part of its normal operation.

- Datastores (such as MySQL or CouchDB)
- Messaging/queueing systems (such as RabbitMQ or Beanstalkd)
- SMTP services for outbound email (such as Postfix)
- caching systems (such as Memcached)
- SMTP services (such as Postmark)
- Metrics-gathering services (such as New Relic or Loggly)
- API-accessible consumer services (such as Twitter, Google Maps, or Last.fm) managed by same app administrator or third parties.

Changing the resource handle in the config should allow to easily swap the services, like switching from local(eg MySQL) service to a third-party provided (MySQL) service.

### SQL

Store database connection details configuration in the environment
`export DATABASE_URL="mysql://user:password@localhost:3306/mydatabase"`

```env
DATABASE_USER=***
DATABASE_PASSWORD=***
DATABASE_HOST=localhost
DATABASE_NAME=***
```

```python
import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

# Get database URL from environment variable
conn = mysql.connector.connect(
    host=os.getenv("DATABASE_HOST"),
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    database=os.getenv("DATABASE_NAME")
)

# Use the connection
cursor = conn.cursor()
cursor.execute("SELECT * FROM mytable")
results = cursor.fetchall()
cursor.close()
conn.close()
```

For simplicity we will be using sqlite database for this project
