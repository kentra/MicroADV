from udataclasses import dataclass, field


# States
@dataclass
class AppState:
    mqtt_connected: bool = False
    wifi_connected: bool = False
