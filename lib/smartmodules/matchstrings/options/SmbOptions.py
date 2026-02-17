#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib.smartmodules.matchstrings.MatchStrings import options_match


options_match['smb'] = {
    'nmap': {
        r'Microsoft Windows system vulnerable to remote code execution \(MS08-067\)\s*(\r\n|\r|\n)\|\s*State: (LIKELY )?VULNERABLE': {
            'name': 'vuln-ms08-067',
            'value': 'true',
        },
        r'Remote Code Execution vulnerability in Microsoft SMBv1 servers \(ms17-010\)\s*(\r\n|\r|\n)\|\s*State: (LIKELY )?VULNERABLE': {
            'name': 'vuln-ms17-010',
            'value': 'true',
        },
        r'SAMBA Remote Code Execution from Writable Share\s*(\r\n|\r|\n)\|\s*State: (LIKELY )?VULNERABLE': {
            'name': 'vuln-sambacry',
            'value': 'true',
        },
    },
    'metasploit': {
        'VULNERABLE to MS17-010': {
            'name': 'vuln-ms17-010',
            'value': 'true',
        },
    },

}

