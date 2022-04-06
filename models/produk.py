from odoo import api, fields, models


class Produk(models.Model):
    _name = 'mebel.produk'
    _description = 'Produk Mebel Yang Kami Punya'

    nama_produk = fields.Char(string='Name')
    jenis_mebel = fields.Char(string='Jenis Mebel')
    gaya = fields.Char(string='Gaya Mebel')
    harga_jadi = fields.Integer(compute='_compute_total', string='Total', store=True)

    produkdetail_ids = fields.One2many(
        comodel_name='mebel.produkdetail',
        inverse_name='produk_id',
        string='Produk Detail')

    @api.depends('produkdetail_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['mebel.bahan'].search([('bahan_id', '=', record.id)]).mapped('harga_bahan_detail'))
            b = sum(self.env['mebel.produksi'].search([('produksi_id', '=', record.id)]).mapped('harga_produksi_detail'))
            record.total = a + b

class ProdukDetail(models.Model):
    _name = 'mebel.produkdetail'
    _description = 'Produk Mebel detail'

    produk_id = fields.Many2one(comodel_name='mebel.produk', string='Produk')

    # based on bahan-id
    bahan_id = fields.Many2one(comodel_name='mebel.bahan', string='Bahan req', required=True)
    harga_bahan_detail = fields.Integer(compute='_compute_harga_bahan_detail', string='harga_bahan')

    @api.depends('bahan_id')
    def _compute_harga_bahan_detail(self):
        for record in self:
            record.harga_bahan_detail = record.bahan_id.harga_bahan

    # based on produksi-id
    produksi_id = fields.Many2one(comodel_name='mebel.produksi', string="Jasa Produksi", required=True)
    harga_produksi_detail = fields.Integer(compute='_compute_harga_produksi_detail', string='harga_produksi')

    @api.depends('produksi_id')
    def _compute_harga_bahan_detail(self):
        for record in self:
            record.harga_produksi_detail = record.produksi_id.harga_produksi