from odoo import api, fields, models, _

class KasStatementLine(models.Model):
    _inherit = 'account.bank.statement.line'

    def create_jurnal(self):
        for transaksi in self:
            # Technical functionality to automatically reconcile by creating a new move line
            vals = {
                'name': transaksi.name,
                'debit': transaksi.amount < 0 and -transaksi.amount or 0.0,
                'credit': transaksi.amount > 0 and transaksi.amount or 0.0,
                'account_id': transaksi.account_id.id,
            }
            transaksi.process_reconciliation(new_aml_dicts=[vals])

    def button_print(self, context=None):
        if self:
        	ids = [self.journal_entry_ids.id]
        	context = dict(context or {}, active_ids=ids, active_model=self.env['account.move']._name)
        	# print"==========context=============",context
        return {
        	'type': 'ir.actions.report.xml',
        	'report_name': 'vit_journal_voucher.account_move_report',
        	'paperformat_id': 'vit_journal_voucher.journal_voucher_paperformat',
        	'context': context,
        	'report_type': 'qweb-pdf',
        	}