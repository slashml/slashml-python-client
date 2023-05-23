Welcome to SlashML
==========================

| **SlashML** is a framework that provides the best performing ML models under one API. This enables the users to rapidly prototype their machine-learning solutions.


Getting Started
---------------

.. code-block:: python

   pip install slashml


Example - Text To Speech
------------------------

.. literalinclude:: ../examples/text_to_speech_sync.py

Examples
--------

You can find other examples `here <https://github.com/slashml/slashml-python-client/tree/main/examples>`_.

API Token
---------

There is a daily limit (throttling) on the number of calls the user performs. The code can run without specifying the API key. The throttling kicks in and prevents new jobs after exceeding 10 calls per minute.

If the user intends on using the service more frequently, it is recommended to generate an token or API key from `here <https://www.slashml.com/settings/api-key>`_. You can pass the API key when creating a model, if you don't the API will still work but you will be throttled.


Services
----------

| We currently support the following machine-learning services:

.. toctree::
   :maxdepth: 1
   :caption: Services
   :name: services
   :glob:

   services/*


Deploying Examples
------------------

- `Deploy Demos <./deployment/dash_render.html>`_: It takes around 2-5 minutes to deploy our demos.

.. toctree::
   :maxdepth: 1
   :caption: Deployment Examples
   :name: deployment_examples
   :hidden:

   ./deployment/dash_render.md


Reference Docs
---------------

| Full documentation on all methods and classes for SlashML.

- `Reference Documentation <./reference.html>`_

.. toctree::
   :maxdepth: 1
   :caption: Reference
   :name: reference
   :hidden:

   ./reference.rst


Additional Resources
---------------------

| Additional resources we think may be useful as you develop your application!

- `Website <https://slashml.com/>`_: Visit our website to manage your slashml account.

- `Twitter <https://twitter.com/slash_ml>`_: Follow us on twitter to receive the latest updates!


.. toctree::
   :maxdepth: 1
   :caption: Additional Resources
   :name: resources
   :hidden:

   Website <https://slashml.com/>
   Twitter <https://twitter.com/slash_ml>
