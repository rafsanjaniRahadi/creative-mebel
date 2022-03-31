from odoo import api, fields, models


class Produk(models.Model):
    _name = 'mebel.produk'
    _description = 'Produk Mebel Yang Kami Punya'

    name_produk = fields.Char(string='Name')
    jenis_mebel = fields.Char(string='Jenis Mebel')
    gaya = fields.Char(string='Gaya Mebel')
    
