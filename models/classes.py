# -*- coding: utf-8 -*-

from odoo import models, fields, api


class classe(models.Model):
    _name = 'schoolmanager.classe'

    name = fields.Char()
    level = fields.Selection([('seconde', 'Seconde'), ('premiere', 'Première'), ('terminal', 'Terminale')])
    teacher_id = fields.Many2one('schoolmanager.teacher', string="Professeur")
    student_ids = fields.One2many('schoolmanager.student', 'class_id', string="Elèves")

    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100
