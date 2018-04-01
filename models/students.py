# -*- coding: utf-8 -*-

import datetime
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class student(models.Model):
	_name = 'schoolmanager.student'

	firstname = fields.Char()
	lastname = fields.Char()
	birthdate = fields.Date()
	age = fields.Integer(compute='_compute_age')
	class_id = fields.Many2one('schoolmanager.classe', string="Classe")

	@api.depends('birthdate')
	def _compute_age(self):
		for record in self:
			now = datetime.date.today()
			birthdate = datetime.datetime.strptime(record.birthdate, '%Y-%m-%d').date()
			record.age = (now-birthdate).days/365