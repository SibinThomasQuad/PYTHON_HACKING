import win32evtlog

def get_event_logs(log_type, max_records):
    events = []
    
    hand = win32evtlog.OpenEventLog(None, log_type)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    
    events_generator = win32evtlog.ReadEventLog(hand, flags, 0)
    
    for event in events_generator:
        events.append(event)
        if len(events) >= max_records:
            break
    
    win32evtlog.CloseEventLog(hand)
    return events

def main():
    log_type = "System"  # Choose the log type ("System", "Application", "Security", etc.)
    max_records = 100  # Specify the maximum number of records to retrieve
    
    events = get_event_logs(log_type, max_records)
    
    for event in events:
        print(f"Event ID: {event.EventID}")
        print(f"Time Generated: {event.TimeGenerated}")
        print(f"Source Name: {event.SourceName}")
        print(f"Description: {event.StringInserts}\n")

if __name__ == "__main__":
    main()
