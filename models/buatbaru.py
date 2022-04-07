from odoo import fields, models, api


class BuatBaru(models.Model):
    _name = 'mebel.buatbaru'
    _description = 'Layanan untuk pembuatan mebel baru'

    name = fields.Char(string='Name', required=False)
    tanggal_pesan = fields.Datetime('Tanggal Pembuatan', default=fields.Datetime.now())
    tanggal_jadi = fields.Date(string='Tanggal Pengiriman')
    qty = fields.Integer(string='Quantity')
    harga = fields.Integer(compute='_compute_harga_total_bb', string='harga')

    # base on produk
    produk_id = fields.Many2one(comodel_name='mebel.produk', string='produk' )

    name_produk = fields.Char(string='Name')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='harga_satuan')

    @api.depends('produk_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.produk_id.harga_jadi

    @api.depends('qty','harga_satuan')
    def _compute_harga_total_bb(self):
        for record in self:
           record.harga_total_bb = record.harga_satuan * record.qty