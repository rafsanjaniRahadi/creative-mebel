from odoo import api, fields, models


class Bahan(models.Model):
    _name = 'mebel.bahan'
    _description = 'segala bahan yang kita pakai'

    name_bahan = fields.Char(string='Name')
    tipe_bahan = fields.Char(string='Tipe Bahan Dasar')
    jumlah_tersedia = fields.Integer(string='Jumlah tersedia')
    harga = fields.Integer(string='Harga Bahan')
    keterangan = fields.Char(string='Bahan Dasar')

    