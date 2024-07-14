<div align="center">
  <a href="https://instagram.com/_mehdisabz_>
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" width="100"/>
  </a>
  <!-- <a href="https://codingyar.com">
    <img src="https://img.shields.io/badge/website-blue?style=for-the-badge&logo=About.me&logoColor=white" width="100"/>
  </a> -->
</div>


# What is this project?
<span><img src="https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=green" /></span>
<span><img src="https://img.shields.io/badge/Docker-2CA5E0?style=flat&logo=docker&logoColor=white" /></span>
<span><img src="https://img.shields.io/badge/PostgreSQL-316192?style=flat&logo=postgresql&logoColor=white" /></span>

This repository contains the source code and resources for the Amer Engineering Group website built with Django.

# Overview

<strong>The Amer Engineering Group website serves as a platform to showcase our services and projects in the field of engineering and construction. It provides information about our company, highlights our expertise, and offers a contact point for potential clients.
</strong>

# Features

<strong>Homepage : </strong>Introduction to Amer Engineering Group and featured services.
<strong>Projects : </strong>Showcase of past and ongoing projects.
<strong>Materials : </strong>Brands and materials used prominently in our projects.
<strong>About Us : </strong>Detailed information about company's history, mission, and values.
<strong>Contact : </strong>Contact details for inquiries.

# Installation

To run the project locally, follow these steps:

Clone the repository:
```bash
git clone https://github.com/your-username/amer-engineering-group.git
```


Then make sure Docker is running.
* If you are on windows click on the Docker Desktop icon and wait for about a minute.

Navigate into the project directory:

```bash
cd amer-engineering-group
```

Then in the project directory run this command:

```bash
docker-compose up --build
```

It will create two containers:
One for Django and one for PostgreSql as the database for the project.
All the required packages will be installed.

### Install a new package.
* Attention:
If you want to install a package for django project you should run this command:

```bash
docker-compose exec web pip install <package-name>
``` 

Don't forget to add the new package to requirements.txt for further use:
```bash
docker-compose exec web pip freeze > requirements.txt
```