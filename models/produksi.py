from odoo import api, fields, models


class Produksi(models.Model):
    _name = 'mebel.produksi'
    _description = 'Proses Pembuatan Mebel'

    nama_produksi = fields.Char(string='Name')
    harga_produksi = fields.Integer(string='Biaya Produksi')
    durasi = fields.Selection(string='Durasi Pembuatan',
                             selection=[('5 Hari Pengerjaan', '5 Hari Pengerjaan'),
                                        ('10 Hari Pengerjaan', '10 Hari Pengerjaan'),
                                        ('15 Hari Pengerjaan', '15 Hari Pengerjaan')])
    