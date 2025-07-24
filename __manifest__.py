{
    "name": "Custom Title and Favicon",
    "version": "1.0",
    "summary": """
        This module customizes title and favicon logo.
    """,
    "description": "Custom Title & Favicon",
    "author": "mhrafin",
    "maintainer": "mhrafin",
    "license": "LGPL-3",
    "depends": ["web"],
    "data": [
        "views/favicon.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "custom-title-and-favicon/static/src/js/favicon.js",
        ],
    },
    "demo": [],
    "installable": True,
    "application": True,
    "auto_install": False,
    "qweb": [],
}
