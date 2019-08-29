# Boilerplate

A boilerplate template to wrap your PyTorch machine learning code as a Flask REST API, complete with Dockerfiles, Tensorboard, etc. This template is designed for classification tasks in PyTorch so minor changes are required for regression tasks. Checkout this simple [text-classification](https://github.com/practicalAI/text-classification) repository for an example of how this boilerplate template can be leveraged.

### Set Up
```bash
pip install cookiecutter invoke requests
cookiecutter gh:practicalAI/boilerplate
```

### Steps
1. Place data in **src/datasets** or have it in S3, etc.
2. Edit the *training.json* configuration file in **src/configs**.
3. Define *requirements* and *setup.py* for your package in **src**.
4. Edit *application.py*, *config.py*, and *wsgi.py* in **src**.
5. Edit *endpoints.py* and *utils.py* functions in **src/api**.
6. Add ML components in **src/{{ cookiecutter.service_name }}**.
7. Add unit and e2e tests in **src/tests**.

### Directory structure
```
{{ cookiecutter.service_name }}/
├── src/                                  - source files
|   ├── api/                                - holds all API scripts
|   |   ├── endpoints.py                      - API endpoint definitions
|   |   └── utils.py                          - utility functions for endpoints
|   ├── configs/                            - configuration files
|   |   ├── logging.json                      - logger configuration
|   |   └── training.json                     - training configuration
|   ├── data/                               - directory to hold datasets
|   ├── {{ cookiecutter.package_name }}/    - ML files
|   |   ├── dataset.py                        - dataset generator functions
|   |   ├── eval.py                           - evaluation on test set
|   |   ├── infer.py                          - inference operations
|   |   ├── load.py                           - load data
|   |   ├── model.py                          - model functions
|   |   ├── split.py                          - split data
|   |   ├── tokenize.py                       - tokenize data
|   |   ├── train.py                          - training operations
|   |   ├── utils.py                          - utilities
|   ├── tests/                              - tests
|   |   ├── e2e/                              - integration tests
|   |   ├── unit/                             - unit tests
|   ├── application.py                      - application script
|   ├── config.py                           - application configuration
|   ├── requirements.txt                    - python package requirements
|   ├── setup.py                            - custom package setup
|   ├── wsgi.py                             - application initialization
├── .dockerignore                         - dockerignore file
├── .gitignore                            - gitignore file
├── Dockerfile                            - Dockerfile for the application
├── CODE_OF_CONDUCT.md                    - code of conduct
├── CODEOWNERS                            - code owner assignments
├── LICENSE                               - license description
└── README.md                             - repository readme
```