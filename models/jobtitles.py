from odoo import api, fields, models, _


class JobTitles(models.Model):
    _name = "hr.jobtitles"
    _description = "Job Titles"
    _rec_name = "name"
    _log_access = False

    #id_jobt = fields.Integer(string='ID',required=True)
    name=fields.Char(string="Name", translate=True,required=True)
    # disabled=fields.Boolean(string='Disabled',required=True,default=False, tracking=True)


