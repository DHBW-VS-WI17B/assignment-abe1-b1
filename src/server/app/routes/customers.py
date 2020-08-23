from flask import Blueprint
from flask import request
from flask import jsonify
from thespian.actors import ActorSystem
from app.enums.customers_action import CustomersActorAction
from app.actors.customers_actor import CustomersActor
from app.classes.customer import Customer
from app.classes.actor_message import ActorMessage

bp = Blueprint("customers", __name__, url_prefix='/api/customers')


@bp.route("/", methods=["POST"])
def add():
    """Add a new customer."""
    try:
        customer_id = request.headers.get('Customer-ID')
        if customer_id:
            return jsonify({'error': "You are not authorized."}), 403
        asys = ActorSystem()
        actor = asys.createActor(actorClass=CustomersActor)
        customer = Customer.from_json(request.get_json())
        payload = {
            'customer': customer
        }
        message = ActorMessage(
            action=CustomersActorAction.CUSTOMERS_ADD, payload=payload, customer_id=customer_id)
        customer = asys.ask(actor, message)
        return "", 204
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@bp.route("/<customer_id>/budget", methods=["GET"])
def get_budget(customer_id):
    """Get the budget of a specific customer."""
    try:
        customer_id = request.headers.get('Customer-ID')
        if not customer_id:
            return jsonify({'error': "You are not authorized."}), 403
        asys = ActorSystem()
        actor = asys.createActor(actorClass=CustomersActor)
        customer_id = request.headers.get('Customer-ID')
        payload = {
            'customer_id': int(customer_id)
        }
        message = ActorMessage(
            action=CustomersActorAction.CUSTOMERS_BUDGET, payload=payload, customer_id=customer_id)
        budget = asys.ask(actor, message)
        return jsonify(budget)
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@bp.route("/<customer_id>/tickets", methods=["POST"])
def get_tickets(customer_id):
    """Get the tickets of a specific customer."""
    try:
        customer_id = request.headers.get('Customer-ID')
        if not customer_id:
            return jsonify({'error': "You are not authorized."}), 403
        asys = ActorSystem()
        actor = asys.createActor(actorClass=CustomersActor)
        customer_id = request.headers.get('Customer-ID')
        payload = {
            'customer_id': int(customer_id),
            # TODO
            'order_date': request.args.get('order_date', default=None, type=int),
            'event_date': request.args.get('event_date', default=None, type=int)
        }
        message = ActorMessage(
            action=CustomersActorAction.CUSTOMERS_TICKETS, payload=payload, customer_id=customer_id)
        tickets_dict = []
        tickets = asys.ask(actor, message)
        for ticket in tickets:
            tickets_dict.append(ticket.__dict__)
        return jsonify(tickets)
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
