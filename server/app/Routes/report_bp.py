from flask import Blueprint

from Controllers.ReportController import index

report_bp = Blueprint('report_bp',__name__)

report_bp.route('/', methods=['Get'])(index)