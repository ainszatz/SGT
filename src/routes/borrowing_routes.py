from flask import Blueprint
from src.controllers.borrowing_controller import create_borrowing_controller, return_borrowing_controller, get_member_borrowing_history_controller

borrowing_routes = Blueprint('borrowing_routes', __name__)

borrowing_routes.route('/api/borrowings', methods=['POST'])(create_borrowing_controller)
borrowing_routes.route('/api/borrowings/<string:borrowing_id>/return', methods=['PUT'])(return_borrowing_controller)
borrowing_routes.route('/api/members/<string:member_id>/borrowings', methods=['GET'])(get_member_borrowing_history_controller)