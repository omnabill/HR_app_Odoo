from odoo import api, fields, models, _


class Qualifications(models.Model):
    _name = "hr.qualifications"
    _description = "Qualifications"
    _rec_name = "name"
    _log_access = False

    #id_qual = fields.Integer(string='ID',required=True)
    name=fields.Char(string="Name", translate=True,required=True)
    type= fields.Selection([('1', 'متوسط'), ('2', 'فوق متوسط'),('3', 'عليا')],string='Type')
    # disabled=fields.Boolean(string='Disabled',required=True,default=False, tracking=True)


