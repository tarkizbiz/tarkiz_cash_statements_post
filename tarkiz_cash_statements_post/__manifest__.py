{
    'name' : 'Cash Statements Auto Post',
    'version' : '10.0.1',
    'summary': 'Cash Statements auto Post and account No Javascript',
    'description': """
                    auto post cash statements in single view without Javascript
                    """,
    'category': 'Accounting',
    'author': 'Tarkiz.Biz',
    'sequence': 11,
    'maintainer': 'Tarkiz',
    'website': '',
    'images': ['static/description/tarkiz_image.png'],
    'depends': ['account','account_cancel','vit_journal_voucher'],
    'data': ['views/cash_view.xml',
             ],
    'demo': [],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}