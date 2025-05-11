## 10. Minimizing Dev/prod parity

> **Keep development, staging, and production as similar as possible***

**Continuous deployment** allows to minimize the gap between development and production.

- A developer may write code which gets deployed in minutes/hours, and the developer who writes the code are closely involved in deploying it and watching its behavior in production.

**There can be tool gap as well mostly because of different tools particularly the backing services being used in development and production.**

*For example, using SQLite locally and PostgreSQL in production; or local process memory for caching in development and Memcached in production.*

- The twelve-factor developer resists the urge to use different backing services between development and production
- It might cause a code that worked and passed tests in development or staging to fail in production.
- Run local environments that closely approximate production environments.
