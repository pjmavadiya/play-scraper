# -*- coding: utf-8 -*-

"""
play_scraper.api

:copyright: (c) 2016 Daniel Liu.
:license: MIT, see LICENSE for more details.

"""

from . import scraper


def details(app_id):
    """Sends a GET request to the app's info page, parses the app's details, and
    returns them as a dict.

    :param app: ID of an app to retrieve details from, e.g. 'com.nintendo.zaaa'
    :return: a dictionary of app details
    """
    s = scraper.PlayScraper()
    return s.details(app_id)


def collection(collection, category=None, **kwargs):
    """Sends a POST request to the collection url, gets each app's details, and
    returns them in a list.

    List of acceptable collections and categories can be found in settings.

    :param collection: the collection ID as a string.
    :param category: the category ID as a string.
    :param results: the number of app results to retrieve
    :param page: the page number, calculates collection start index. is limited
        to page * results <= 500
    :param detailed: if True, sends request per app for full detail
    :return: a list of app dictionaries
    """
    s = scraper.PlayScraper()
    return s.collection(collection, category, **kwargs)


def developer(developer, **kwargs):
    """Sends a POST request to the developer's page, extracts their apps' basic
    info, and returns them in a list.

    :param developer: developer name to retrieve apps from, e.g. 'Disney'
    :param results: the number of app results to retrieve
    :param detailed: if True, sends request per app for full detail
    :return: a list of app dictionaries
    """
    s = scraper.PlayScraper()
    return s.developer(developer, **kwargs)


def suggestions(query):
    """Sends a GET request to the Play Store's suggestion API and returns up to
    five autocompleted suggested query strings in a list.

    :param query: the query string to get autocomplete suggestions
    :return: a list of suggestion strings
    """
    s = scraper.PlayScraper()
    return s.suggestions(query)