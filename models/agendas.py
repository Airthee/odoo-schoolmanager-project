# -*- coding: utf-8 -*-

from odoo import models, fields, api


class agenda(models.Model):
    _name = 'schoolmanager.agenda'

    date_start = fields.Datetime()
    date_stop = fields.Datetime()
    room = fields.Char()
    class_id = fields.Many2one('schoolmanager.classe', string="Classe")
    course_id = fields.Many2one('schoolmanager.course', string="Cours")
    
