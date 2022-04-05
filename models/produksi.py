from odoo import api, fields, models


class Produksi(models.Model):
    _name = 'mebel.produksi'
    _description = 'Proses Pembuatan Mebel'

    nama_produksi = fields.Char(string='Name')
    harga_produksi = fields.Integer(string='Biaya Produksi')
    durasi = fields.Integer(string='Durasi Pembuatan')
    