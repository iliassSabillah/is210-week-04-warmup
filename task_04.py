#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module returns whether or not we have too many kittens."""

def too_many_kittens(kittens, litterboxes, catfood):
    """This function determines whether or not we have too many kittens.

    Args:
        kittens (int): Number of kittens.
        litterboxes (int): Number of litterboxes.
        catfood (bool): a boolean representing whether or not any catfood exists.

    Returns:
        bool: returns whether or not we have too many kittens.

    Examples:

        >>>print(too_many_kittens(12,12, False))
        >>>True
    """
    
    if not (litterboxes >= kittens and catfood):
        return True
    else:
        return False