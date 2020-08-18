"""Customers 
"""
from flask import Blueprint
from flask import request
from flask import jsonify
from thespian.actors import ActorSystem
from app.enums.actor_name import ActorName
from app.enums.customers_actor_action import CustomersActorAction
from app.actors.customers_actor import CustomersActor
from app.classes.customer import Customer
from app.classes.actor_message import ActorMessage

bp = Blueprint("customers", __name__, url_prefix='/api/customers')


@bp.route("/", methods=["POST"])
def add():
    """ add Customer """
    try:
        asys = ActorSystem()
        actor = asys.createActor(CustomersActor, None,
                                 ActorName.CUSTOMERS_ACTOR)
        customer = Customer.from_json(request.get_json())
        payload = {
            'customer': customer
        }
        message = ActorMessage(CustomersActorAction.CUSTOMERS_ADD, payload)
        customer = asys.ask(actor, message)
        return "", 204
    except Exception as ex:
        return jsonify({'error': str(ex)})


@bp.route("/<customer_id>", methods=["GET"])
def get(customer_id):
    """ get customer by id

    Args:
        customer_id (int): customer Id

    Returns:
        Customer: Customer that has specific id
    """
    try:
        asys = ActorSystem()
        actor = asys.createActor(CustomersActor, None,
                                 ActorName.CUSTOMERS_ACTOR)
        payload = {
            'customer_id': int(customer_id)
        }
        message = ActorMessage(CustomersActorAction.CUSTOMERS_GET, payload)
        customer = asys.ask(actor, message)
        return jsonify(customer)
    except Exception as ex:
        return jsonify({'error': str(ex)})


@bp.route("/<customer_id>/budget", methods=["POST"])
def get_budget(customer_id):
    """ get budget of specific customer

    Args:
        customer_id (int): customer Id

    Returns:
        int: budget of the customer
    """
    try:
        asys = ActorSystem()
        actor = asys.createActor(CustomersActor, None,
                                 ActorName.CUSTOMERS_ACTOR)
        payload = {
            'customer_id': int(customer_id)
        }
        message = ActorMessage(CustomersActorAction.CUSTOMERS_BUDGET, payload)
        budget = asys.ask(actor, message)
        return jsonify(budget)
    except Exception as ex:
        return jsonify({'error': str(ex)})


@bp.route("/<customer_id>/tickets", methods=["POST"])
def get_tickets(customer_id):
    """ get tickets of the customer

    Args:
        customer_id (int): customer id

    Returns:
        Ticket(): List of ticket filtered by order date or event date
    """
    try:
        asys = ActorSystem()
        actor = asys.createActor(CustomersActor, None,
                                 ActorName.CUSTOMERS_ACTOR)
        payload = {
            'customer_id': int(customer_id),
            'order_date': request.args.get('order_date', default=None, type=int),
            'event_date': request.args.get('event_date', default=None, type=int)
        }
        message = ActorMessage(CustomersActorAction.CUSTOMERS_TICKETS, payload)
        tickets_dict = []
        tickets = asys.ask(actor, message)
        for ticket in tickets:
            tickets_dict.append(ticket.__dict__)
        return jsonify(tickets)
    except Exception as ex:
        return jsonify({'error': str(ex)})
