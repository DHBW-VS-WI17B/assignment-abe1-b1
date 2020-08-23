from flask import Blueprint
from flask import request
from flask import jsonify
from thespian.actors import ActorSystem, ActorExitRequest
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
        actor = asys.createActor(actorClass=EventsActor)
        customer_id = request.headers.get('Customer-ID')
        message = ActorMessage(
            action=EventsActorAction.EVENTS_LIST, customer_id=customer_id)
        events = asys.ask(actor, message)
        # asys.tell(actor, ActorExitRequest())
        events_dict = []
        for event in events:
            events_dict.append(Event.to_dict(event))
        return jsonify(events)
    except Exception as ex:
        return jsonify({'error': str(ex)})


@bp.route('/', methods=['POST'])
def add():
    """Add a new event."""
    try:
        asys = ActorSystem()
        actor = asys.createActor(actorClass=EventsActor)
        event = Event.from_json(request.get_json())
        payload = {
            'event': event
        }
        message = ActorMessage(
            action=EventsActorAction.EVENTS_ADD, payload=payload)
        asys.tell(actor, message)
        # asys.tell(actor, ActorExitRequest())
        return '', 204
    except Exception as ex:
        return jsonify({'error': str(ex)})


@bp.route('/<event_id>', methods=['GET'])
def get(event_id):
    """Get event by ID."""
    try:
        asys = ActorSystem()
        actor = asys.createActor(actorClass=EventsActor)
        customer_id = request.headers.get('Customer-ID')
        payload = {
            'event_id': int(event_id)
        }
        message = ActorMessage(
            action=EventsActorAction.EVENTS_GET, payload=payload, customer_id=customer_id)
        response = asys.ask(actor, message)
        if response.error:
            return jsonify({'error': str(response.error)})
        # asys.tell(actor, ActorExitRequest())
        return jsonify(Event.to_dict(response.payload.get('event')))
    except Exception as ex:
        return jsonify({'error': str(ex)})


@bp.route('/<event_id>/tickets', methods=['GET'])
def get_tickets(event_id):
    """Get the tickets of a specific event."""
    try:
        asys = ActorSystem()
        actor = asys.createActor(actorClass=EventsActor)
        payload = {
            'event_id': int(event_id)
        }
        message = ActorMessage(
            action=EventsActorAction.EVENTS_TICKETS, payload=payload)
        events_dict = []
        events = asys.ask(actor, message)
        # asys.tell(actor, ActorExitRequest())
        for event in events:
            events_dict.append(Event.to_dict(event))
        return jsonify(events)
    except Exception as ex:
        return jsonify({'error': str(ex)})


@bp.route('/<event_id>/purchase', methods=['POST'])
def purchase(event_id):
    """Purchase tickets for a specific event."""
    try:
        asys = ActorSystem()
        actor = asys.createActor(actorClass=EventsActor)
        customer_id = request.headers.get('Customer-ID')
        payload = {
            'event_id': int(event_id),
            'quantity': request.get_json().get('quantity')
        }
        message = ActorMessage(
            action=EventsActorAction.EVENTS_PURCHASE, payload=payload, customer_id=customer_id)
        asys.tell(actor, message)
        # asys.tell(actor, ActorExitRequest())
        return '', 204
    except Exception as ex:
        return jsonify({'error': str(ex)})
