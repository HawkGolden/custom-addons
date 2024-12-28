from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class Calculator(models.Model):
    _name = 'calcu_basic.operation'
    _description = 'Operación de la calculadora'

    operation_type = fields.Selection([
        ('add', 'Suma'),
        ('subtract', 'Resta'),
        ('multiply', 'Multiplicación'),
        ('divide', 'División')
    ], string='Tipo de Operación')

    operand1 = fields.Float('Primer Operando')
    operand2 = fields.Float('Segundo Operando')
    result = fields.Float('Resultado', compute="calculate_result")
    date = fields.Datetime('Fecha de la operación', default=fields.Datetime.now)

    @api.depends('operand1', 'operand2', 'operation_type')
    def calculate_result(self):
        for record in self:
            _logger.info("Calculando resultado para: %s %s %s", record.operand1, record.operation_type, record.operand2)
            if record.operation_type == 'add':
                record.result = record.operand1 + record.operand2
            elif record.operation_type == 'subtract':
                record.result = record.operand1 - record.operand2
            elif record.operation_type == 'multiply':
                record.result = record.operand1 * record.operand2
            elif record.operation_type == 'divide':
                if record.operand2 != 0:
                    record.result = record.operand1 / record.operand2
                else:
                    record.result = 0  # Para evitar la división por 0
            _logger.info("Resultado calculado: %s", record.result)

    def cancel_operation(self):
        self.operand1 = 0
        self.operand2 = 0
        self.result = 0
