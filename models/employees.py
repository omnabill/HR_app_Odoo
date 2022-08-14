from odoo import api, fields, models, _
from odoo.exceptions import  ValidationError

class Employees(models.Model):
    _name = "hr.employees"
    _description = "Employees"
    _rec_name= "name"
    _log_access = False

#    id_emp = fields.Integer(string='ID',required=True)

    name = fields.Char(string="Name", translate=True,required=True)
    mobile1= fields.Char(string="Mobile Phone",required=True)
    emp_image = fields.Binary(string="Photo")

    mobile2 = fields.Char(string="Mobile 2")
    department = fields.Many2one("hr.departments",string="Department",required=True)
    email = fields.Char(string="Email")
    jobtitle= fields.Many2one("hr.jobtitles",string="Job Title")
    qualification= fields.Many2one("hr.qualifications",string="Qualifications")
    empdate=fields.Date(string="Employment Date")
    birthdate = fields.Date(string="Birth Date")
    city_id = fields.Many2one(comodel_name='res.country.state', string='City', tracking=True)
    address = fields.Char(string="Address")
    NatID= fields.Char(string="National ID")
    insnumber= fields.Integer(string="Insurance Number")
    bankacc= fields.Char(string="Bank Account")
    empstatus =fields.Selection([('1','يعمل حاليا'),('2','مستقيل'),('3','اجازة بدون اجر')],string="Emp Status")
    salary = fields.Float(string='Salary',digits=(6,2) , tracking=True)

    @api.model
    def create(self, vals):
            dept=vals['department']
            h_emp = self.env['hr.employees'].search_count([('department','=',dept)])
            dep_max= self.env['hr.departments'].search([('id','=',dept)])
            print(dep_max.minemp,h_emp)

            if h_emp>dep_max.minemp :
                raise ValidationError(_("Can't Create New Record as this department Reach it's maximum"))
            return super(Employees, self).create(vals)

