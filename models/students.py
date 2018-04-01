# -*- coding: utf-8 -*-

import datetime
from odoo import models, fields, api

class student(models.Model):
    _name = 'schoolmanager.student'

    firstname = fields.Char()
    firstname = fields.Char()
    birthdate = fields.Date()
    age = fields.Integer(compute='_compute_age')
    class_id = fields.Many2one('schoolmanager.classe', string="Classe")

    @api.depends('birthdate')
    def _compute_age(self):
    	for record in self:
	    	now = datetime.date.today()
	    	delta = now - record.birthdate
	    	record.age = delta.days/365