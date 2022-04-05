from odoo import api, fields, models


class Pembuatan(models.Model):
    _name = 'mebel.pembuatan'
    _description = 'Layanan untuk pembuatan/pengadaan barang baru'
    
    buatbarudetail_ids = fields.One2many(comodel_name='mebel.buatbaru', inverse_name='pembuatan_ids', string='buatbaru')

    nama_mebel = fields.Char(string='Nama Mebel', required=True)
    tanggal_pesan = fields.Datetime('Tanggal Pemesanan', default=fields.Datetime.now())
    tanggal_jadi = fields.Date(string='Tanggal Pengiriman')
    # QTY = fields.Char(string='Jumlah Mebel')
    total = fields.Integer(compute='_compute_total', string='Total', store=True)

    @api.depends('buatbarudetail_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['mebel.buatbaru'].search([('bahan_id', '=', record.id)]).mapped('harga_bahan'))
            b = sum(self.env['mebel.buatbaru'].search([('bahan_id', '=', record.id)]).mapped('harga_jasa'))
            record.total = a + b


class BuatBaru(models.Model):
    _name = 'mebel.buatbaru'
    _description = 'New Description'

    pembuatan_ids = fields.Many2one(comodel_name='mebel.pembuatan', string='Pembuatan')

    # based on bahan-id
    bahan_id = fields.Many2one(comodel_name='mebel.bahan', string='bahan')
    bahan_used = fields.Char(string='Harga - bahan')
    harga_bahan = fields.Integer(compute='_compute_harga_perbahan', string='Harga - bahan')

    # total_harga_bahan = fields.Integer(string="Total - Harga Bahan")

    @api.depends('bahan_id')
    def _compute_harga_perbahan(self):
        for record in self:
            record.harga_bahan = record.panggung_id.harga

    # based on produksi-id
    produksi_id = fields.Many2one(comodel_name='mebel.produksi', string='produksi')
    jasa_used = fields.Char(string='Name')
    harga_jasa = fields.Integer(compute='_compute_harga_perproduksi', string='Harga - Jasa')

    # total_harga_jasa = fields.Integer(string="Total - Harga Jasa")

    @api.depends('produksi_id')
    def _compute_harga_perproduksi(self):
        for record in self:
            record.harga_jasa = record.panggung_id.harga_produksi
