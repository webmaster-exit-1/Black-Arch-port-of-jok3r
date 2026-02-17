#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib.smartmodules.matchstrings.MatchStrings import products_match


WIG_REGEXP = r'{}\s*[VERSION]\s*Platform' 
WIG_REGEXP2 = r'- Found platform {}(\s*[VERSION])?'


products_match['http']['web-appserver'] = {
    'Adobe/Coldfusion': {
        'wappalyzer': 'Adobe ColdFusion',
        'clusterd': [
            'Matched [0-9]+ fingerprints for service coldfusion',
            r'ColdFusion Manager\s*\(version [VERSION]\)',
            r'ColdFusion Manager\s*\(version Any\)',
        ],
        'wig': [
            WIG_REGEXP.format('ColdFusion'),
            WIG_REGEXP2.format('Coldfusion'),
        ],
    },
    'Apache/Axis2': {
        'clusterd': [
            'Matched [0-9]+ fingerprints for service axis2',
            r'Axis2 Server\s*\(version [VERSION]\)',
            r'Axis2 Server\s*\(version Any\)',
        ],
    },
    'Apache/Tomcat': {
        'wappalyzer': 'Apache Tomcat',
        'banner': r'Apache Tomcat(\s+[VERSION])?',
        'clusterd': [
            'Matched [0-9]+ fingerprints for service tomcat',
            r'Tomcat (Manager|Admin)?\s*\(version [VERSION]\)',
            r'Tomcat (Manager|Admin)?\s*\(version Any\)',
        ],
        'wig': [
            WIG_REGEXP.format('Tomcat'),
            WIG_REGEXP2.format('Tomcat'),
        ],
    },
    'Eclipse/Jetty': {
        'wappalyzer': 'Jetty',
        'banner': r'Jetty(\s*[VERSION])?',
    },
    'Jboss': {
        'wappalyzer': 'JBoss Application Server',
        'banner': r'JBoss (service httpd|Administrator|WildFly Application Server|Enterprise Application Platform)(\s*[VERSION])?',
        # Clusterd example:
        # [2018-11-15 05:04PM] Matched 5 fingerprints for service jboss
        # [2018-11-15 05:04PM]    JBoss Web Manager (version 5.1)
        # [2018-11-15 05:04PM]    JBoss EJB Invoker Servlet (version Any)
        # [2018-11-15 05:04PM]    JBoss HTTP Headers (Unreliable) (version 5.0)
        # [2018-11-15 05:04PM]    JBoss JMX Invoker Servlet (version Any)
        # [2018-11-15 05:04PM]    JBoss RMI Interface (version Any)
        # [2018-11-15 05:04PM] Fingerprinting completed.
        # [2018-11-15 05:04PM] Loading auxiliary for 'jboss'...
        # [2018-11-15 05:04PM] Finished at 2018-11-15 05:04PM
        'clusterd': [
            'Matched [0-9]+ fingerprints for service jboss',
            # Multiline regexp
            r'JBoss (JMX Console|Web Console|Web Manager|Management|JMX Invoker Servlet|EJB Invoker Servlet|RMI Interface|Status Page|HTTP Headers \(Unreliable\))\s*\(version [VERSION]\)',
            r'JBoss (JMX Console|Web Console|Web Manager|Management|JMX Invoker Servlet|EJB Invoker Servlet|RMI Interface|Status Page|HTTP Headers \(Unreliable\))\s*\(version Any\)',
        ],
        'wig': [
            WIG_REGEXP.format('jBoss'),
            WIG_REGEXP2.format('jBoss'),
        ],
    },
    'Jenkins': {
        'wappalyzer': 'Jenkins',
        'banner': r'Jenkins(\s*[VERSION])?',
    },
    'Oracle/Glassfish': {
        'wappalyzer': 'GlassFish',
        'banner': r'GlassFish(\s*(Open Source Edition|Communications Server|Administration Console|application server))?(\s*[VERSION])?',
        'clusterd': [
            'Matched [0-9]+ fingerprints for service glassfish',
            r'GlassFish (Admin|JMX RMI|HTTP Headers \(Unreliable\))\s*\(version [VERSION]\)',
            r'GlassFish (Admin|JMX RMI|HTTP Headers \(Unreliable\))\s*\(version Any\)',
        ],
    },
    'Oracle/Weblogic Server': {
        'wappalyzer': 'Weblogic Server',
        'banner': r'WebLogic (applications server|admin httpd|httpd|Server)(\s+[VERSION])?',
        'nmap': r'weblogic-t3-info: T3 protocol in use \(WebLogic version: [VERSION]\)',
        'clusterd': [
            'Matched [0-9]+ fingerprints for service weblogic',
            r'WebLogic Admin Console (\(https\))?\s*\(version [VERSION]\)',
            r'WebLogic Admin Console (\(https\))?\s*\(version Any\)',
        ],
    },
    'Railo': {
        'clusterd': [
            'Matched [0-9]+ fingerprints for service railo',
            r'Railo (Server|Web Administrator|Server Administrator|AJP)\s*\(version [VERSION]\)',
            r'Railo (Server|Web Administrator|Server Administrator|AJP)\s*\(version Any\)',
        ],
    },
    'Websphere Application Server': {
        'wappalyzer': 'Websphere Application Server',
        'banner': r'WebSphere (Application Server|httpd)(\s*[VERSION])?',
    },
    'Zope': {
        'wappalyzer': 'Zope',
        'banner': r'Zope httpd(\s*[VERSION])?',
        'wig': [
            WIG_REGEXP.format('Zope'),
            WIG_REGEXP2.format('Zope'),
        ],
    },
}