from tracking_client import Event


class ValidatedEvent(Event):
    @Event.duration.setter
    def duration(self, duration):
        if not isinstance(duration, int):
            raise ValueError("duration must be an integer")

        Event.duration.fset(self, duration)