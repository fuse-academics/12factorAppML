## 6. Stateless Processes

> **Execute the app as one or more stateless processes**

- App should run as a stateless and share-nothing process *(locally or in a production deploy)*. 
- Any data that needs to persist must be stored in a *stateful backing service, typically a database*. 
- The memory space or filesystem of the process can be used as a brief, single-transaction cache such as for downloading a large file, operating on it, storing results of database, etc. 

*A restart can wipe out this memory, or the future request or job could be served by a different process without access to this memory.*

- Some web systems rely on “sticky sessions” – that is, caching user session data in memory of the app’s process and expecting future requests from the same visitor to be routed to the same process. 

**Sticky sessions are a violation of twelve-factor and should never be used or relied upon.**

- Session state data is a good candidate for a datastore that offers time-expiration, such as Memcached or Redis.

<details>
<summary>Redis</summary>
</details>
