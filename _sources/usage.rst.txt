.. _usage:

Usage
=====

``python-logo`` can be used in two ways:

1. As a Python module
2. As a web application

For frontend details, see the ``frontend/README.md`` file in the repository.

As a Python Module
------------------

.. code-block:: python

   import python_logo

   sample_code = "fd 10 bk 20"

   # Generate commands one by one
   logo_runner = python_logo.run(sample_code)
   for command in logo_runner:
       print(command)
       # Example output:
       # {'command': 'forward', 'value': 10}
       # {'command': 'backward', 'value': 20}

   # Or get them all at once
   logo_runner = python_logo.run(sample_code)
   commands = list(logo_runner)
   print(commands)
   # [{'command': 'forward', 'value': 10}, {'command': 'backward', 'value': 20}]

As a Web Application
--------------------

1. **Build the frontend**:

   .. code-block:: bash

      npm install --prefix frontend/
      npm run build --prefix frontend/

2. **Run the application**:

   .. code-block:: bash

      # If installed via pip
      python app.py

      # If using Poetry
      poetry run python app.py
