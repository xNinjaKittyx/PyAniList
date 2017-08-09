.. PyAniList documentation master file, created by
   sphinx-quickstart on Mon Aug  7 23:00:22 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PyAniList documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Welcome to PyAniList Documentation!


Table of Contents
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Introduction
============
Starting a AniList Session is fairly simple. To create a session, use AniListClient::

    anilist_client = AniListClient(client_id, client_secret, client_pin, loop=None)
