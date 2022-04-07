from odoo import api, fields, models, tools


class Produksi(models.Model):
    _name = 'mebel.produksi'
    _description = 'Proses Pembuatan Mebel'

    name = fields.Char(string='name')
    harga_produksi = fields.Integer(string='Biaya Produksi')
    durasi = fields.Selection(string='Durasi Pembuatan',
                             selection=[('5 hari pengerjaan', '5 Hari Pengerjaan'),
                                        ('10 hari pengerjaan', '10 Hari Pengerjaan'),
                                        ('15 hari pengerjaan', '15 Hari Pengerjaan')])
    