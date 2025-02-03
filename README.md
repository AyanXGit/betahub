# BetaHub

BetaHub is a Python application that customizes and schedules alerts for reminders, appointments, or system events on Windows. Users can set alerts with custom messages and optionally include sound notifications.

## Features

- Schedule alerts for specific future dates and times.
- Customize alert messages.
- Optionally enable sound notifications for alerts.
- Manage alerts by adding and removing them from the schedule.

## Requirements

- Python 3.x
- Windows OS (due to the use of `winsound` for sound alerts)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/betahub.git
   ```

2. Navigate to the project directory:
   ```bash
   cd betahub
   ```

3. Run the Python script:
   ```bash
   python betahub.py
   ```

## Usage

- To create an alert, call the `add_alert` method with a name, a `datetime` object, a message, and an optional boolean for sound.
- To remove an alert, use the `remove_alert` method with the alert's name.
- Run the scheduler by invoking the `run` method.

### Example

```python
from datetime import datetime, timedelta

bh = BetaHub()
future_time = datetime.now() + timedelta(seconds=60)
bh.add_alert("Meeting Reminder", future_time, "Don't forget the meeting at 3 PM.", sound=True)
bh.run()
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.