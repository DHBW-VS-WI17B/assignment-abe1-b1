from flask import Blueprint
from flask import request
from flask import jsonify
from thespian.actors import ActorSystem
from app.enums.actor_name import ActorName
from app.enums.events_action import EventsActorAction
from app.actors.events_actor import EventsActor
from app.classes.event import Event
from app.classes.actor_message import ActorMessage

bp = Blueprint('events', __name__, url_prefix='/api/events')


@bp.route('/', methods=['GET'])
def index():
    """Get event list."""
    try:
        asys = ActorSystem()
        actor = asys.createActor(EventsActor, None, ActorName.EVENTS_ACTOR)
        message = ActorMessage(EventsActorAction.EVENTS_LIST, None)
        events_dict = []
        events = asys.ask(actor, message)
        for event in events:
            events_dict.append(event.__dict__)
        return jsonify(events)
    except Exception as ex:
        return jsonify({'error': str(ex)})


@bp.route('/', methods=['POST'])
def add():
    """Add a new event."""
    try:
        asys = ActorSystem()
        actor = asys.createActor(EventsActor, None, ActorName.EVENTS_ACTOR)
        event = Event.from_json(request.get_json())
        payload = {
            'event': event
        }
        message = ActorMessage(EventsActorAction.EVENTS_ADD, payload)
        asys.tell(actor, message)
        return '', 204
    except Exception as ex:
        return jsonify({'error': str(ex)})


@bp.route('/<event_id>', methods=['GET'])
def get(event_id):
    """Get event by ID."""
    try:
        asys = ActorSystem()
        actor = asys.createActor(EventsActor, None, ActorName.EVENTS_ACTOR)
        payload = {
            'event_id': int(event_id)
        }
        message = ActorMessage(EventsActorAction.EVENTS_GET, payload)
        event = asys.ask(actor, message)
        return jsonify(event.__dict__)
    except Exception as ex:
        return jsonify({'error': str(ex)})


@bp.route('/<event_id>/tickets', methods=['GET'])
def get_tickets(event_id):
    """Get the tickets of a specific event."""
    try:
        asys = ActorSystem()
        actor = asys.createActor(EventsActor, None, ActorName.EVENTS_ACTOR)
        payload = {
            'event_id': int(event_id)
        }
        message = ActorMessage(EventsActorAction.EVENTS_TICKETS, payload)
        events = asys.ask(actor, message)
        events_dict = []
        events = asys.ask(actor, message)
        for event in events:
            events_dict.append(event.__dict__)
        return jsonify(events)
    except Exception as ex:
        return jsonify({'error': str(ex)})


@bp.route('/<event_id>/purchase', methods=['POST'])
def purchase(event_id):
    """Purchase tickets for a specific event."""
    try:
        asys = ActorSystem()
        actor = asys.createActor(EventsActor, None, ActorName.EVENTS_ACTOR)
        payload = {
            'event_id': int(event_id),
            'quantity': request.get_json().get('quantity')
        }
        message = ActorMessage(EventsActorAction.EVENTS_PURCHASE, payload)
        asys.tell(actor, message)
        return '', 204
    except Exception as ex:
        return jsonify({'error': str(ex)})
