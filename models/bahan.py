from odoo import api, fields, models


class Bahan(models.Model):
    _name = 'mebel.bahan'
    _description = 'segala bahan yang kita pakai'

    name_bahan = fields.Char(string='Name')
    keterangan = fields.Char(string='Bahan Dasar')
    tipe_bahan = fields.Char(string='Tipe Bahan Dasar')
    harga = fields.Integer(string='Harga Bahan')
    jumlah_tersedia = fields.Integer(string='Jumlah tersedia')
    
    