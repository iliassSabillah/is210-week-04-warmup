#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module is returning a logical comparison."""

def defaults(my_required, my_optional=True):
    """This function compares between my_optional and my_required .

    Args:
        my_required (bool): a boolean representing a required argument.
        my_optional (bool, optional): a boolean representing an optional argument.

    Returns:
        bool: returns a boolean representing a comparison between my_required and my_optional.

    Examples:

        >>>print(defaults(False))
        >>>False

        >>>print(defaults(True))
        >>>True

        >>>print(defaults(True, True))
        >>>True
    """

    return my_optional is my_required