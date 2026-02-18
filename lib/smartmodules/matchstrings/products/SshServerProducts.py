#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib.smartmodules.matchstrings.MatchStrings import products_match


products_match['ssh']['ssh-server'] = {
    'Openssh': {
        'banner': r'OpenSSH(\s+[VERSION])?',
    },
    'Dropbear SSH': {
        'banner': r'Dropbear sshd(\s+[VERSION])?',
    }
}