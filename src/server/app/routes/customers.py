from flask import Blueprint
from flask import request
from flask import jsonify
from thespian.actors import ActorSystem
from app.enums.actor_name import ActorName
from app.enums.events_actor_action import EventsActorAction
from app.actors.events_actor import EventsActor

bp = Blueprint("customers", __name__, url_prefix='/api/customers')


@bp.route("/", methods=["POST"])
def index():
    asys = ActorSystem()
    actor = asys.createActor(CustomersActor, None, ActorName.CUSTOMER_ACTOR)
    message = {
        "action": EventsActorAction.CUSTOMERS_ADD
        "payload": request.get_json()
    }
    asys.tell(actor, message)
    return '', 204


@bp.route("/<customer_id>/budget", methods=["POST"])
def add():
    asys = ActorSystem()
    actor = asys.createActor(CustomersActor, None, ActorName.CUSTOMER_ACTOR)
    message = {
        "action": EventsActorAction.CUSTOMERS_BUDGET
    }
    budget = asys.ask(actor, message, 2)
    return budget

@bp.route("/<customer_id>/tickets?order_date=&event_date", methods=["POST"])
def add():
    asys = ActorSystem()
    actor = asys.createActor(CustomersActor, None, ActorName.CUSTOMER_ACTOR)
    message = {
        "action": EventsActorAction.CUSTOMERS_TICKETS,
        "payload": request.get_json()
    }
    tickets = asys.ask(actor, message, 2)
    return jsonify(tickets)