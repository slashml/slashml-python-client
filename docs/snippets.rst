Snippets
========

.. code-block:: python

   # some code here

   def another():
      return "this is a method"

Ref: https://sublime-and-sphinx-guide.readthedocs.io/en/latest/code_blocks.html


.. literalinclude:: ../examples/text_to_speech_sync.py
   :linenos:

Ref: https://devopstutodoc.readthedocs.io/en/stable/documentation/doc_generators/sphinx/rest_sphinx/code/literalinclude/literalinclude.html


Get the latest news at `CNN`_.

.. _CNN: http://cnn.com/


Test hyperlink: `Stack Overflow home <https://stackoverflow.com/>`_.


Ref: https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html#links-to-external-web-pages


Adding .md into .rst files
.. mdinclude:: ../README.md

but m2r2 needs to be installed first


| A comprehensive list of LLMs, systems, and products integrated with LangChain:


.. toctree::
   :maxdepth: 1
   :glob:

   integrations/*
