import pytest
from datetime import datetime
from scheduler import SuperFrog, Event

def test_assign_event():
    super = SuperFrog("Gustavo")
    event1 = Event(1, datetime(2025, 5, 5, 14), datetime(2025, 5, 5, 16))
    event2 = Event(2, datetime(2025, 5, 5, 17), datetime(2025, 5, 5, 18))
    
    assert super.assign_event(event1) == True
    assert super.assign_event(event2) == True
    assert len(super.schedule) == 2
    
def test_time_conflict():
    super = SuperFrog("Gustavo")
    event1 = Event(1, datetime(2025, 5, 5, 14), datetime(2025, 5, 5, 16))
    event2 = Event(2, datetime(2025, 5, 5, 15), datetime(2025, 5, 5, 17))
    
    assert super.assign_event(event1) == True
    assert super.assign_event(event2) == False
    assert len(super.schedule) == 1