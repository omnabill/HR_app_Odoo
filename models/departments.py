from odoo import api, fields, models, _


class Departments(models.Model):
    _name = "hr.departments"
    _description = "Departments"
    _rec_name = "name"
    _log_access = False

   # id_dep = fields.Integer(string='ID',required=True)
    name=fields.Char(string="Name", translate=True,required=True)
    parent_id= fields.Many2one("hr.departments",string='Parent Department')
    manager_id= fields.Many2one("hr.employees",string="Manager")
    minemp = fields.Integer(string="Maximum no. of EMPLOYEES")
    photo = fields.Binary(string="Photo")
    # disabled=fields.Boolean(string='Disabled',required=True,default=False, tracking=True)
    emp_assigned = fields.Float(string='Emp_assigned', compute='_compute_emp_assigned')
    perc= fields.Float(string='Percent of Employees assigned', compute='_compute_perc_assigned')

    def _compute_emp_assigned(self):
        for rec in self:
            dep_max = self.env['hr.employees'].search_count([('department', '=', rec.id)])
            rec.emp_assigned = dep_max

    def _compute_perc_assigned(self):
        for rec in self:
            rec.perc = (rec.emp_assigned/rec.minemp)*100