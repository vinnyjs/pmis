# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models
import odoo.addons.decimal_precision as dp
from odoo.exceptions import ValidationError



class AnalyticResourcePlanLine(models.Model):

    _inherit = 'analytic.resource.plan.line'

    def _prepare_purchase_request_line(self, pr_id, line):
        res = super(AnalyticResourcePlanLine, self).\
            _prepare_purchase_request_line(pr_id, line)
        res.update(product_qty=line.qty_left)
        return res

    @api.multi
    def _make_purchase_request(self):
        res = {}
        for line in self:
            if line.qty_left <= 0:
                continue
            else:
                res = super(AnalyticResourcePlanLine, line).\
                    _make_purchase_request()
        return res