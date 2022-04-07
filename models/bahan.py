from odoo import api, fields, models, tools


class Bahan(models.Model):
    _name = 'mebel.bahan'
    _description = 'segala bahan yang kita pakai'

    name = fields.Char(string='name')
    tipe_bahan = fields.Char(string='Tipe Bahan Dasar')
    jumlah_tersedia = fields.Integer(string='Jumlah tersedia')
    harga_bahan = fields.Integer(string='Harga Bahan')
    keterangan = fields.Char(string='Keterangan')
    
