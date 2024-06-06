import pytest
from unittest.mock import Mock

from python.atividades.atividade14_email_service import EventHandler

def test_handle_event_valid_event():
    email_service_mock = Mock()
    event_handler = EventHandler(email_service_mock)
    event = {'type': 'test_event'}

    event_handler.handle_event(event)

    email_service_mock.send_email.assert_called_once_with('test@example.com', 'Event Occurred', str(event))

def test_handle_event_invalid_event():
    email_service_mock = Mock()
    event_handler = EventHandler(email_service_mock)
    event = 'invalid_event'

    with pytest.raises(ValueError):
        event_handler.handle_event(event)