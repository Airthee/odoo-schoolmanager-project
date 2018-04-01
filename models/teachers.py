# -*- coding: utf-8 -*-

from odoo import models, fields, api


class teacher(models.Model):
    _name = 'schoolmanager.teacher'
    _inherit = 'res.partner'

    classe_ids = fields.One2many('schoolmanager.classe', 'teacher_id', string="Classes")