import time
import sched
from datetime import datetime, timedelta
import winsound

class BetaHub:
    def __init__(self):
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.alerts = {}

    def add_alert(self, name, alert_time, message, sound=False):
        """
        Adds an alert to the scheduler.
        
        :param name: Name of the alert
        :param alert_time: Datetime object when the alert should trigger
        :param message: Message to be displayed when the alert triggers
        :param sound: Boolean indicating if a sound should be played
        """
        delay = (alert_time - datetime.now()).total_seconds()
        if delay < 0:
            raise ValueError("Alert time must be in the future")
        
        event = self.scheduler.enter(delay, 1, self.trigger_alert, (name, message, sound))
        self.alerts[name] = event
        print(f"Alert '{name}' scheduled for {alert_time}.")

    def trigger_alert(self, name, message, sound):
        print(f"Alert '{name}': {message}")
        if sound:
            winsound.Beep(1000, 500)  # Beep at 1000 Hz for 500 ms

    def remove_alert(self, name):
        """
        Removes an alert from the scheduler.
        
        :param name: Name of the alert to be removed
        """
        if name in self.alerts:
            event = self.alerts.pop(name)
            self.scheduler.cancel(event)
            print(f"Alert '{name}' removed.")
        else:
            print(f"No alert found with name '{name}'.")

    def run(self):
        """
        Runs the scheduler.
        """
        print("Starting the scheduler...")
        try:
            self.scheduler.run()
        except KeyboardInterrupt:
            print("Scheduler stopped.")

if __name__ == "__main__":
    bh = BetaHub()
    # Example usage
    future_time = datetime.now() + timedelta(seconds=10)
    bh.add_alert("Test Alert", future_time, "This is a test alert", sound=True)

    bh.run()