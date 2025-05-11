# Gitflow Workflow

This project follows the [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) for structured branching and release management.

![Img](https://wac-cdn.atlassian.com/dam/jcr:cc0b526e-adb7-4d45-874e-9bcea9898b4a/04%20Hotfix%20branches.svg?cdnVersion=2710)

## Branches

- **main**: Production-ready code. Only stable, tested releases.
- **develop**: Integration branch for features. Reflects the latest development state.

## Supporting Branches

- **feature/\***:
    - Created from: `develop`
    - Purpose: New features
    - Merged into: `develop`
    - Naming: `feature/user-login`

- **release/\***:
    - Created from: `develop`
    - Purpose: Prepare for a production release (e.g., version bump, final testing)
    - Merged into: `main` and `develop`
    - Naming: `release/1.0.0`

- **hotfix/\***:
    - Created from: `main`
    - Purpose: Critical fixes to production
    - Merged into: `main` and `develop`
    - Naming: `hotfix/urgent-fix`

- **bugfix/\*** (optional):
    - Created from: `develop`
    - Purpose: Fixing non-critical bugs
    - Merged into: `develop`
    - Naming: `bugfix/fix-login-error`

## Pull Request Rules

- All changes go through PRs and must be reviewed.
- CI must pass before merging.
- PR titles follow branch naming conventions.

---
