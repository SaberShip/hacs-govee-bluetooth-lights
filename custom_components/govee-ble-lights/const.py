from homeassistant.const import Platform

DOMAIN = "govee_ble_lights"
PLATFORMS: list[str] = [
    Platform.LIGHT
]
DEVICE_TYPES = ["Other", "H6053", "H6127"]
