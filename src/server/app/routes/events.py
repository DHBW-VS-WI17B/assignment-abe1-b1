from flask import Blueprint
from flask import request
from flask import jsonify
from thespian.actors import ActorSystem
from app.enums.actor_name import ActorName
from app.enums.events_actor_action import EventsActorAction
from app.actors.events_actor import EventsActor
from app.classes.event import Event
from app.classes.actor_message import ActorMessage

bp = Blueprint('events', __name__, url_prefix='/api/events')


@bp.route('/', methods=['GET'])
def index():
    asys = ActorSystem()
    actor = asys.createActor(EventsActor, None, ActorName.EVENT_ACTOR)
    message = ActorMessage(EventsActorAction.EVENTS_LIST, None)
    events = asys.ask(actor, message)
    return jsonify(events)


@bp.route('/', methods=['POST'])
def add():
    asys = ActorSystem()
    actor = asys.createActor(EventsActor, None, ActorName.EVENT_ACTOR)
    event = Event.from_json(request.get_json())
    payload = {
        'event': event
    }
    message = ActorMessage(EventsActorAction.EVENTS_ADD, payload)
    asys.tell(actor, message)
    return '', 204


@bp.route('/<event_id>', methods=['GET'])
def get(event_id):
    asys = ActorSystem()
    actor = asys.createActor(EventsActor, None, ActorName.EVENT_ACTOR)
    payload = {
        'event_id': int(event_id)
    }
    message = ActorMessage(EventsActorAction.EVENTS_GET, payload)
    events = asys.ask(actor, message)
    return jsonify(events)


@bp.route('/<event_id>/tickets', methods=['GET'])
def get_tickets(event_id):
    asys = ActorSystem()
    actor = asys.createActor(EventsActor, None, ActorName.EVENT_ACTOR)
    payload = {
        'event_id': int(event_id),
        'order_date': request.args.get('order_date', default=None, type=int),
        'event_date': request.args.get('event_date', default=None, type=int)
    }
    message = ActorMessage(EventsActorAction.EVENTS_TICKETS, payload)
    events = asys.ask(actor, message)
    return jsonify(events)


@bp.route('/<event_id>/purchase', methods=['POST'])
def purchase(event_id):
    asys = ActorSystem()
    actor = asys.createActor(EventsActor, None, ActorName.EVENT_ACTOR)
    payload = {
        'event_id': int(event_id),
        'quantity': request.get_json().get('quantity')
    }
    message = ActorMessage(EventsActorAction.EVENTS_PURCHASE, payload)
    asys.tell(actor, message)
    return '', 204
