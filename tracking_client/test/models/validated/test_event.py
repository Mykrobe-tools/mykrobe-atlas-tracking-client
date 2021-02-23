from hypothesis import given
from hypothesis.strategies import floats, integers, text, sampled_from, composite
from pytest import raises

from tracking_client.models.validated.event import ValidatedEvent


@composite
def event_names(draw):
    return draw(sampled_from(['de-contamination', 'QC', 'variant-calling', 'prediction', 'bigsi-building', 'distance-calculation']))


@given(integers(), event_names(), text(), text(), floats(), floats(), text())
def test_event_durations_cannot_be_floats(event_id, name, software, software_version, start_time, duration, command):
    with raises(ValueError):
        ValidatedEvent(event_id, name, software, software_version, start_time, duration, command)


@given(integers(), event_names(), text(), text(), floats(), integers(), text())
def test_event_durations_can_be_integers(event_id, name, software, software_version, start_time, duration, command):
    ValidatedEvent(event_id, name, software, software_version, start_time, duration, command)