from odoo import fields, models, api


class BuatBaru(models.Model):
    _name = 'mebel.buatbaru'
    _description = 'Layanan untuk pembuatan mebel baru'

    produkdetail_ids= fields.One2many(comodel_name='mebel.produkdetail',
                                      inverse_name='buatbaru_id',
                                      string='Produk Detail',
                                      required=False)

    name = fields.Char(string='Name')
    tanggal_pesan = fields.Datetime('Tanggal Pembuatan', default=fields.Datetime.now())
    tanggal_jadi = fields.Date(string='Tanggal Pengiriman')
    qty = fields.Integer(string='Quantity')
    total = fields.Integer(compute='_compute_total', string='harga')

    @api.depends('produkdetail_ids', 'qty')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['mebel.produkdetail'].search([('produk_id', '=', record.id)]).mapped('harga_satuan'))
            record.total = a * record.qty

class ProdukDetail(models.Model):
    _name = 'mebel.produkdetail'
    _description = 'Detail untuk pembuatan mebel baru'

    buatbaru_id = fields.Many2one(comodel_name='mebel.buatbaru',string='Buatbaru_id',required=False)

    # base on produk
    produk_id = fields.Many2one(comodel_name='mebel.produk', string='produk')

    name = fields.Char(string='Nama Produk')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='harga_satuan')

    @api.depends('produk_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.produk_id.harga_jadi







