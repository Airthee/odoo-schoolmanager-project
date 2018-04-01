# -*- coding: utf-8 -*-

from odoo import models, fields, api


class course(models.Model):
    _name = 'schoolmanager.course'

    name = fields.Char()
