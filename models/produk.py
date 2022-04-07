from odoo import api, fields, models, tools

class Produk(models.Model):
    _name = 'mebel.produk'
    _description = 'Produk Mebel Yang Kami Punya'

    bahandetail_ids = fields.One2many(
        comodel_name='mebel.bahandetail',
        inverse_name='produkb_id',
        string='Bahan Detail')

    produksidetail_ids = fields.One2many(
        comodel_name='mebel.produksidetail',
        inverse_name='produkp_id',
        string='Produksi Detail')

    name = fields.Char(string='name', required=True)
    harga_jadi = fields.Integer(compute='_compute_total', string='Total', store=True)

    @api.depends('bahandetail_ids', 'produksidetail_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['mebel.bahandetail'].search([('produkb_id', '=', record.id)]).mapped('harga'))
            b = sum(self.env['mebel.produksidetail'].search([('produkp_id', '=', record.id)]).mapped('harga'))
            record.harga_jadi = a + b

class BahanDetail(models.Model):
    _name = 'mebel.bahandetail'
    _description = 'Bahan Mebel detail'

    produkb_id = fields.Many2one(comodel_name='mebel.produk', string='Produk')

    # based on bahan-id
    bahan_id = fields.Many2one(comodel_name='mebel.bahan', string='Bahan req')
    name = fields.Char(string='name Bahan')
    qty_require = fields.Integer(string='Qty required')
    harga = fields.Integer(compute='_compute_harga', string='harga')
    harga_bahan_detail = fields.Integer(compute='_compute_harga_bahan_detail', string='harga_bahan_detail')

    @api.depends('bahan_id')
    def _compute_harga_bahan_detail(self):
        for record in self:
            record.harga_bahan_detail = record.bahan_id.harga_bahan

    @api.depends('harga_bahan_detail','qty_require')
    def _compute_harga(self):
        for record in self:
               record.harga = record.harga_bahan_detail * record.qty_require



class ProduksiDetail(models.Model):
    _name = 'mebel.produksidetail'
    _description = 'Produksi Mebel Detail'

    produkp_id = fields.Many2one(comodel_name='mebel.produk', string='Produk')

    # based on produksi-id
    produksi_id = fields.Many2one(comodel_name='mebel.produksi', string="Jasa Produksi")
    name = fields.Char(string='name Produksi')
    durasi = fields.Selection(string='Durasi Pembuatan',
                             selection=[('5 hari pengerjaan', '5 Hari Pengerjaan'),
                                        ('10 hari pengerjaan', '10 Hari Pengerjaan'),
                                        ('15 hari pengerjaan', '15 Hari Pengerjaan')])

    harga = fields.Integer(compute='_compute_harga', string='harga')
    harga_produksi_detail = fields.Integer(compute='_compute_harga_produksi_detail', string='harga_produksi')

    @api.depends('produksi_id')
    def _compute_harga_produksi_detail(self):
        for record in self:
            record.harga_produksi_detail = record.produksi_id.harga_produksi

    @api.depends('harga_produksi_detail')
    def _compute_harga(self):
        for record in self:
               record.harga = record.harga_produksi_detail

