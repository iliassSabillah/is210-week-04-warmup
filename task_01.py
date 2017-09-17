#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Function that knows what you mean and returns a string .

    Args:
        wink (str): a string to be multiplied by numwink.
        numwink (int, optional): an integer that is multiplied by wink, Default: 2 

    Returns:
        str: returns winks and nudges multiplied by numwink and concatenated with commas.
    
    Examples:
        >>>print(know_what_i_mean('wink ', 4))
        >>>Know what I mean? wink wink wink wink, nudge nudge nudge nudge
    """

    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr