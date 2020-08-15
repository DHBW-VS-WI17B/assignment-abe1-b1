from flask import Blueprint
from flask import request
from flask import jsonify
from thespian.actors import ActorSystem
from app.enums.actor_name import ActorName
from app.enums.events_actor_action import EventsActorAction
from app.actors.events_actor import EventsActor

bp = Blueprint("events", __name__, url_prefix='/api/events')


@bp.route("/", methods=["GET"])
def index():
    asys = ActorSystem()
    actor = asys.createActor(EventsActor, None, ActorName.EVENT_ACTOR)
    message = {
        "action": EventsActorAction.EVENTS_LIST
    }
    events = asys.ask(actor, message, 2)
    return jsonify(events)


@bp.route("/", methods=["POST"])
def add():
    asys = ActorSystem()
    actor = asys.createActor(EventsActor, None, ActorName.EVENT_ACTOR)
    message = {
        "action": EventsActorAction.EVENTS_ADD,
        "payload": request.get_json()
    }
    asys.tell(actor, message)
    return '', 204


@bp.route("/<event_id>", methods=["GET"])
def get(event_id):
    asys = ActorSystem()
    actor = asys.createActor(EventsActor, None, ActorName.EVENT_ACTOR)
    message = {
        "action": EventsActorAction.EVENTS_GET,
        "payload": event_id
    }
    events = asys.ask(actor, message, 2)
    return jsonify(events)


@bp.route("/<event_id>/purchase?count", methods=["POST"])
def purchase(event_id):
    asys = ActorSystem()
    actor = asys.createActor(EventsActor, None, ActorName.EVENT_ACTOR)
    message = {
        "action": EventsActorAction.EVENTS_PURCHASE,
        "payload": event_id, count
    }
    asys.tell(actor, message)
    return '', 204


@bp.route("/<event_id>/tickets", methods=["GET"])
def get(event_id):
    asys = ActorSystem()
    actor = asys.createActor(EventsActor, None, ActorName.EVENT_ACTOR)
    message = {
        "action": EventsActorAction.EVENTS_GET_TICKETS,
        "payload": event_id
    }
    events = asys.ask(actor, message)
    return jsonify(events)

