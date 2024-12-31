from flask import Blueprint
from src.controllers.member_controller import register_member_controller, get_member_borrowings_controller

member_routes = Blueprint('member_routes', __name__)

member_routes.route('/api/members', methods=['POST'])(register_member_controller)
member_routes.route('/api/members/<string:member_id>/borrowings', methods=['GET'])(get_member_borrowings_controller)
