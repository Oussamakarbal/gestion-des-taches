from odoo import models, fields

class TpTache(models.Model):
    _name = 'tp.tache'
    _description = 'Gestion des taches simples'

    name = fields.Char(string="Nom de la tâche", required=True)
    description = fields.Text(string="Description")
    responsable = fields.Char(string="Responsable")
    date_echeance = fields.Date(string="Date d'échéance")
    est_terminee = fields.Boolean(string="Terminée ?", default=False)