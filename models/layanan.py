from odoo import api, fields, models


class Layanan(models.Model):
    _name = 'mebel.layanan'
    _description = 'Layanan mebel'

    nama_mebel = fields.Char(string='Nama Mebel', required=True)
    tanggal_pesan = fields.Datetime('Tanggal Pembuatan', default=fields.Datetime.now())
    tanggal_jadi = fields.Date(string='Tanggal Pengiriman')
    total = fields.Integer(compute='_compute_total', string='Total', store=True)

    buatbarudetail_ids = fields.One2many(comodel_name='mebel.buatbaru', inverse_name='layanan_id', string='buatbaru')

    # @api.depends('buatbarudetail_ids')
    # def _compute_total(self):
    #     for record in self:
    #         a = sum(self.env['mebel.buatbaru'].search([('bahan_id', '=', record.id)]).mapped('harga_bahan'))
    #         b = sum(self.env['mebel.buatbaru'].search([('bahan_id', '=', record.id)]).mapped('harga_jasa'))
    #         record.total = a + b


class BuatBaru(models.Model):
    _name = 'mebel.buatbaru'
    _description = 'New Description'

    layanan_id = fields.Many2one(comodel_name='mebel.layanan', string='layanan')

    # base on produk
    produk_id = fields.Many2one(comodel_name='mebel.produk', string='produk' )

    nama_produk = fields.Char(string='Name')
    harga_total = fields.Integer(compute='_compute_harga', string='harga')
    qty = fields.Integer(string='Quantity')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='harga_satuan')

    @api.depends('produk_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.produk_id.harga_jadi

    @api.depends('qty','harga_satuan')
    def _compute_harga_total(self):
        for record in self:
           record.harga_total = record.harga_satuan * record.qty