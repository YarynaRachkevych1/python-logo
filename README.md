<a id="readme-top"></a>



<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/YarynaRachkevych1/python-logo">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">python-logo</h3>

  <p align="center">
    Python Logo interpreter with frontend made in Svelte.
    <br />
    <br />
    <a href="https://github.com/YarynaRachkevych1/python-logo">View Demo</a>
    ·
    <a href="https://github.com/YarynaRachkevych1/python-logo/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/YarynaRachkevych1/python-logo/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#features">Features</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#as-a-python-module">As a Python module</a></li>
        <li><a href="#as-a-web-application">As a web application</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![python-logo screenshot][product-screenshot]][product-screenshot]

This project is created for the *Innovative Projects by Nokia* subject on [UWR][uwr-url] studies. It features a [Logo][logo-url] language interpreter, a [Flask][flask-url] backend and a [Svelte][svelte-url] frontend.

<a id="features"></a>
### Features

- **TO-DO**

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Make sure you have the following installed:
- **Python**: Version 3.10 or higher
- **Node.js** (optional, for web application): Version 18 or higher
- [**Poetry**][poetry-url] (optional): For dependency management

### Installation

You can install the project in two ways: using `pip` or `poetry`.

#### Using pip

1. Clone the repository:

   ```sh
   git clone https://github.com/YarynaRachkevych1/python-logo.git
   cd python-logo
   ```

2. Create a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the project with dependencies:

   ```sh
   pip install .
   ```

#### Using Poetry

1. Clone the repository:

   ```sh
   git clone https://github.com/YarynaRachkevych1/python-logo.git
   cd python-logo
   ```

2. Install the project with dependencies:

   ```sh
   poetry install
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE -->
## Usage

You can use the project in two ways: as a Python module or as a web application.
For more information about the frontend, see the [frontend/README.md][frontend-readme-url] file.

### As a Python module

```python
import python_logo

sample_code = "fd 10 bk 20"

# Generate commands to execute them one by one.
logo_runner = python_logo.run(sample_code)
for command in logo_runner:
    print(command)
    # {'command': 'forward', 'value': 10}
    # {'command': 'backward', 'value': 20}

# Or get them all at once.
logo_runner = python_logo.run(sample_code)
commands = list(logo_runner)
print(commands)
# [{'command': 'forward', 'value': 10}, {'command': 'backward', 'value': 20}]
```

### As a web application

1. Build the frontend:

   ```sh
   npm install --prefix frontend/
   npm run build --prefix frontend/
   ```

2. Run the application:

   ```sh
   python app.py  # Using pip
   poetry run python app.py  # Using Poetry
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Before commiting, please ensure you've installed pre-commit hooks:

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

### Top contributors:

<a href="https://github.com/YarynaRachkevych1/python-logo/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=YarynaRachkevych1/python-logo" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE][license-url] for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/YarynaRachkevych1/python-logo.svg?style=for-the-badge
[contributors-url]: https://github.com/YarynaRachkevych1/python-logo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/YarynaRachkevych1/python-logo.svg?style=for-the-badge
[forks-url]: https://github.com/YarynaRachkevych1/python-logo/network/members
[stars-shield]: https://img.shields.io/github/stars/YarynaRachkevych1/python-logo.svg?style=for-the-badge
[stars-url]: https://github.com/YarynaRachkevych1/python-logo/stargazers
[issues-shield]: https://img.shields.io/github/issues/YarynaRachkevych1/python-logo.svg?style=for-the-badge
[issues-url]: https://github.com/YarynaRachkevych1/python-logo/issues
[license-shield]: https://img.shields.io/github/license/YarynaRachkevych1/python-logo.svg?style=for-the-badge
[license-url]: https://github.com/YarynaRachkevych1/python-logo/blob/main/LICENSE
[product-screenshot]: images/screenshot.png
[logo-url]: https://en.wikipedia.org/wiki/Logo_(programming_language)
[uwr-url]: https://rekrutacja.uni.wroc.pl/kierunek/informatyka-i-stopnia-stacjonarne-licencjackie-i-inzynierskie
[flask-url]: https://flask.palletsprojects.com/en/stable
[svelte-url]: https://svelte.dev
[poetry-url]: https://python-poetry.org
[frontend-readme-url]: frontend/README.md
