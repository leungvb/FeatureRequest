# Feature Request Application

> A web application that allows IWS employees to add a client's 'feature requests' to an existing piece of software.

 IWS employees are able to prioritize 'feature requests' that clients would like to have added to a piece of existing software.
 The IWS employee is able to add a description, due date, priority number (0 being least important to 9 being very urgent) as well as
 product area and which client requested the feature.

 Employees are able to view a table with all of the feature requests from all of the clients, and order them via any of the attributes (title, client, priority...etc.)
 Feature Requests with higher priority have an urgent badge while tasks with lower priority have a 'save for later' badge.

 ## Table of Contents

- [Pre-Requisites](#prerequisites)
- [Install](#install)
- [Usage](#usage)
- [Running Tests](#tests)
- [Deployment Notes](#deployment)
- [Known Issues/To Do](#issues)
- [Content](#content)


## Install

Create a virtual environment with python 3.7:

```sh
virtualenv venv --python=python3.7
```

Activate the virtual environment:

```sh
. venv/bin/activate
```

Install all requirements from requirements.txt:

```sh
pip install -r requirements.txt
```

