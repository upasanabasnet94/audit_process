# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Checklist(models.Model):
    _inherit = 'project.task'
    _name='project.task'


    # _rec_name='step'
    checklist1=fields.Many2many('checklist.check','task',string='Check list')


    checklist1_steps=fields.One2many('audit.checklist','checklist2_steps',string='Department')
    task_dep=fields.Many2one('audit.department',string='Department')






class Descriptions(models.Model):
    _inherit = 'project.project'



class check(models.Model):
    _name='audit.checklist'
    checklist2_steps=fields.Many2one('project.task', string='stepsss')





class check123(models.Model):
    _inherit='checklist.steps'
    _name='checklist.steps'



class check12345(models.Model):
    _inherit='checklist.check'
    _name='checklist.check'

    task=fields.Many2one('project.task',string='Task')
    select = fields.Boolean(string='Done')
    remark=fields.Char(string="Remarks")

class department(models.Model):
    _name='audit.department'
    _rec_name='department'
    department=fields.Char(string='Department')
    depart_id=fields.One2many('project.task','task_dep')


