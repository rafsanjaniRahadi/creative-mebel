from odoo import api, fields, models


class Bahan(models.Model):
    _name = 'mebel.bahan'
    _description = 'segala bahan yang kita pakai'

    nama_bahan = fields.Char(string='Nama bahan')
    tipe_bahan = fields.Char(string='Tipe Bahan Dasar')
    jumlah_tersedia = fields.Integer(string='Jumlah tersedia')
    harga_bahan = fields.Integer(string='Harga Bahan')
    keterangan = fields.Char(string='Keterangan')

    