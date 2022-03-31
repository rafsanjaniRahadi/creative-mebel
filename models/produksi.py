from odoo import api, fields, models


class Produksi(models.Model):
    _name = 'mebel.produksi'
    _description = 'Proses Pembuatan Mebel'

    name_produksi = fields.Char(string='Name')
    biaya_produksi = fields.Integer(string='Biaya Produksi')
    duration = fields.Integer(string='Durasi Pembuatan (Jam)')
    