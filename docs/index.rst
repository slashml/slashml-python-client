Welcome to SlashML
==========================

| **SlashML** is a framework that provides the best performing ML models under one API. This enables the users to rapidly prototype their machine-learning solutions.


Quick Start
---------------


To quickly play around with the model we recommend using the Python SDK client. You can install the client using pip.

.. code-block:: python

   pip install slashml

Example - Text To Speech
------------------------

.. literalinclude:: ../examples/text_to_speech_sync.py

Example - Text Summarization
------------------------

.. literalinclude:: ../examples/summarize_sync.py

Example - Speech to Text
------------------------

.. literalinclude:: ../examples/speech_to_text_sync.py

Example - Model Deployment
------------------------
.. literalinclude:: ../examples/deploy_model/hugging_face_transformer/deploy_hugging_face_transformer.py

Examples
--------

You can find production ready examples here `here <https://github.com/slashml/slashml-python-client/tree/main/examples>`_.


API Token
---------

There is a daily limit (throttling) on the number of calls the user performs. The code can run without specifying the API key. The throttling kicks in and prevents new jobs after exceeding 10 calls per minute.

If the user intends on using the service more frequently, it is recommended to generate a token or API key from `here <https://www.slashml.com/settings/api-key>`_. You can pass the API key when creating a model, if you don't the API will still work but you will be throttled.


Deploying the above Examples
------------------

- `Deploy Demos <./deployment/dash_render>`_: It takes around 2-5 minutes to deploy our demos.

.. toctree::
   :maxdepth: 1
   :caption: Deployment Examples
   :name: deployment_examples
   :hidden:

   ./deployment/dash_render.md

Python SDK
---------------

| Complete documentation on all methods and classes for SlashML.

.. toctree::
   :maxdepth: 1
   :caption: Python SDK Reference
   :name: reference

   ./reference/sdk_reference.rst

Model Deployment
---------------

| Complete documentation on all methods and classes for SlashML.

.. toctree::
   :maxdepth: 1
   :caption: Model Deployment Reference
   :glob:

   ./model_deployment/*


Full API Reference
----------

Models on SlashML can be used in languages other than Python. The full API reference can be found here. If you would like to create a client in another language, please contact us at `faizank@slashml.com`. We would love to help you out!. 🙏
 
.. toctree::
   :maxdepth: 1
   :caption: API Reference
   :glob:

   api_reference/*


Use Cases
---------------

| This section contains some of the use-cases that we have found for our services.

.. toctree::
   :maxdepth: 1
   :caption: Use-Cases
   :name: use-cases
   :glob:

   use-cases/*


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
