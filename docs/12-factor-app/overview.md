## The Twelve-Factor App

For Projects that extend to a web app or SaaS app, [The Twelve-Factor App](https://12factor.net/) methodology can be helpful.

1. [Codebase](codebase.md): One codebase tracked in revision control, many deploys
2. [Dependencies](dependency.md): Explicitly declare and isolate dependencies
3. [Config](config.md): Store config in the environment
4. [Backing services](backing.md): Treat backing services as attached resources
5. [Build, release, run](build.md): Strictly separate build and run stages
6. [Processes](stateless.md): Execute the app as one or more stateless processes
7. [Port binding](port.md): Export services via port binding
8. [Concurrency](concurrency.md): Scale out via the process model
9. [Disposability](disposability.md): Maximize robustness with fast startup and graceful shutdown
10. [Dev/prod parity](parity.md): Keep development, staging, and production as similar as possible
11. [Logs](logging.md): Treat logs as event streams
12. [Admin processes](admin.md): Run admin/management tasks as one-off processes