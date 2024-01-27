# python-package-template

Opinionated but very simple project template to get started quickly with building a python package.

No difficult cookiecutter setup scripts, just 3 simple steps:

1. Click on the green "Use this template" button on the top right of this page
2. Clone the project to your local machine
3. Where needed adjust license, author, package name, etc.

This template uses:

- `poetry` for dependency management
- `docker` for devcontainer setup
- `github` actions for CI/CD
- `black` for code formatting
- `ruff` for linting
- `gh-action-pypi-publish` for directly publishing your project to PyPi.

If you plan on publishing to PyPI, see [publishing to PyPI with a Trusted Publisher][publish-pypi] for more information on how to setup your project. You will also have to make a `release` environment inside your GitHub repository. See [using environments for deployment][github-env] for more information.

Based on frenck's and klaasnicolaas's CI/CD work, so credits to them!

<!-- MARKDOWN LINKS & IMAGES -->
[publish-pypi]: https://docs.pypi.org/trusted-publishers/
[github-env]: https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment
