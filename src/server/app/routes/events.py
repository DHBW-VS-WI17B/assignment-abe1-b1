from flask import Blueprint
from flask import request
from flask import jsonify
from thespian.actors import ActorSystem
from app.enums.events_action import EventsActorAction
from app.actors.events_actor import EventsActor
from app.classes.event import Event
from app.classes.actor_message import ActorMessage

bp = Blueprint('events', __name__, url_prefix='/api/events')


@bp.route('/', methods=['GET'])
def index():
    """Get event list."""
    try:
        customer_id = request.headers.get('Customer-ID')
        asys = ActorSystem()
        actor = asys.createActor(actorClass=EventsActor)
        message = ActorMessage(action=EventsActorAction.EVENTS_LIST,
                               customer_id=customer_id)
        response = asys.ask(actor, message)
        if response.error:
            return jsonify({'error': str(response.error.message)}), response.error.http_code
        events = response.payload.get('events')
        events_dict = []
        for event in events:
            events_dict.append(Event.to_dict(event))
        return jsonify(events_dict)
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@bp.route('/', methods=['POST'])
def add():
    """Add a new event."""
    try:
        customer_id = request.headers.get('Customer-ID')
        if customer_id:
            return jsonify({'error': "You do not have permissions."}), 403
        asys = ActorSystem()
        actor = asys.createActor(actorClass=EventsActor)
        event = Event.from_json(request.get_json())
        payload = {
            'event': event
        }
        message = ActorMessage(action=EventsActorAction.EVENTS_ADD,
                               payload=payload)
        response = asys.ask(actor, message)
        if response.error:
            return jsonify({'error': str(response.error.message)}), response.error.http_code
        return '', 204
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@bp.route('/<event_id>', methods=['GET'])
def get(event_id):
    """Get event by ID."""
    try:
        customer_id = request.headers.get('Customer-ID')
        asys = ActorSystem()
        actor = asys.createActor(actorClass=EventsActor)
        payload = {
            'event_id': int(event_id)
        }
        message = ActorMessage(action=EventsActorAction.EVENTS_GET,
                               payload=payload, customer_id=customer_id)
        response = asys.ask(actor, message)
        if response.error:
            return jsonify({'error': str(response.error.message)}), response.error.http_code
        return jsonify(Event.to_dict(response.payload.get('event')))
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@bp.route('/sales', methods=['GET'])
def get_sales():
    """Get the number of tickets sold per event."""
    try:
        customer_id = request.headers.get('Customer-ID')
        if customer_id:
            return jsonify({'error': "You do not have permissions."}), 403
        asys = ActorSystem()
        actor = asys.createActor(actorClass=EventsActor)
        message = ActorMessage(action=EventsActorAction.EVENTS_SALES)
        response = asys.ask(actor, message)
        if response.error:
            return jsonify({'error': str(response.error.message)}), response.error.http_code
        return jsonify(response.payload.get('sales_dict'))
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@bp.route('/<event_id>/purchase', methods=['POST'])
def purchase(event_id):
    """Purchase tickets for a specific event."""
    try:
        customer_id = request.headers.get('Customer-ID')
        if not customer_id:
            return jsonify({'error': "You do not have permissions."}), 403
        asys = ActorSystem()
        actor = asys.createActor(actorClass=EventsActor)
        customer_id = request.headers.get('Customer-ID')
        payload = {
            'event_id': int(event_id),
            'quantity': int(request.get_json().get('quantity'))
        }
        message = ActorMessage(action=EventsActorAction.EVENTS_PURCHASE,
                               payload=payload, customer_id=customer_id)
        response = asys.ask(actor, message)
        if response.error:
            return jsonify({'error': str(response.error.message)}), response.error.http_code
        return '', 204
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
