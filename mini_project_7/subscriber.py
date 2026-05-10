"""
subscriber.py — ECRIO_BMS Mini Project 7
──────────────────────────────────────────
MQTT Subscriber Script.

What this does:
  1. Connects to the same public MQTT broker (broker.emqx.io)
  2. Subscribes to the topic "ecrio/bms/messages"
  3. Prints every message received with a local timestamp
  4. Runs continuously until Ctrl+C is pressed
  5. Handles connection errors gracefully

MQTT Concept:
  Publisher  →  Broker  →  Subscriber
  (publisher.py) (server)  (this file)

Run in Terminal 2 FIRST, then start publisher.py in Terminal 1:
    python subscriber.py
"""

import paho.mqtt.client as mqtt
import logging
from datetime import datetime

# ── Logging Setup ──────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("MQTT-Subscriber")

# ── MQTT Configuration ─────────────────────────────────────────────────────────
# Must match the publisher settings exactly
BROKER = "broker.emqx.io"
PORT   = 1883
TOPIC  = "ecrio/bms/messages"   # topic to subscribe to
QOS    = 1                       # Quality of Service level

# ── Message counter ────────────────────────────────────────────────────────────
received_count = 0


# ── Callback Functions ─────────────────────────────────────────────────────────

def on_connect(client, userdata, flags, reason_code, properties=None):
    """
    Called automatically when the subscriber connects to the broker.
    We subscribe to the topic HERE (inside on_connect) so that
    subscriptions are restored automatically if the connection drops.
    """
    if reason_code == 0:
        logger.info(f"✅  Connected to broker: {BROKER}:{PORT}")
        # Subscribe to our custom topic
        client.subscribe(TOPIC, qos=QOS)
        logger.info(f"👂  Subscribed to topic: '{TOPIC}'")
        logger.info("Waiting for messages... (Press Ctrl+C to stop)")
        logger.info("─" * 55)
    else:
        logger.error(f"❌  Connection failed. Reason code: {reason_code}")


def on_message(client, userdata, message):
    """
    Called automatically every time a new message arrives on the subscribed topic.

    Args:
        message.topic   : The topic the message was published to.
        message.payload : The raw bytes of the message body.
        message.qos     : Quality of Service level used.
    """
    global received_count
    received_count += 1

    # Decode the payload from bytes → string
    payload = message.payload.decode("utf-8")

    # Record local receive time
    recv_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n  ┌─ Message #{received_count} received at {recv_time}")
    print(f"  │  Topic   : {message.topic}")
    print(f"  │  QoS     : {message.qos}")
    print(f"  └─ Payload : {payload}")


def on_disconnect(client, userdata, disconnect_flags, reason_code=None, properties=None):
    """Called when the subscriber disconnects from the broker."""
    if reason_code != 0:
        logger.warning(f"⚠️  Unexpected disconnect. Reason code: {reason_code}")
    else:
        logger.info("Disconnected from broker.")


def on_subscribe(client, userdata, mid, reason_codes, properties=None):
    """Called when the broker confirms our subscription."""
    logger.debug(f"Subscription confirmed. Mid: {mid}, Reason codes: {reason_codes}")


# ── Main Subscriber Logic ──────────────────────────────────────────────────────

def run_subscriber():
    """Create MQTT client, connect, subscribe, and listen forever."""

    # ── Create client instance ────────────────────────────────────────────────
    client = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2,
        client_id="ecrio_bms_subscriber",
    )

    # ── Attach callbacks ──────────────────────────────────────────────────────
    client.on_connect    = on_connect
    client.on_message    = on_message
    client.on_disconnect = on_disconnect
    client.on_subscribe  = on_subscribe

    print("\n" + "=" * 55)
    print("  📻  ECRIO_BMS MQTT Subscriber")
    print(f"  Broker : {BROKER}:{PORT}")
    print(f"  Topic  : {TOPIC}")
    print("=" * 55 + "\n")

    # ── Connect to broker ─────────────────────────────────────────────────────
    try:
        logger.info(f"Connecting to {BROKER}:{PORT} ...")
        client.connect(BROKER, PORT, keepalive=60)
    except Exception as exc:
        logger.error(f"Could not connect to broker: {exc}")
        logger.error("Check your internet connection and try again.")
        return

    # ── loop_forever() blocks and handles all network I/O ─────────────────────
    # It will automatically reconnect if the connection drops.
    # Press Ctrl+C to exit.
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        logger.info(
            f"\n🛑  Subscriber stopped. "
            f"Total messages received: {received_count}"
        )
    finally:
        client.disconnect()
        logger.info("Disconnected cleanly. Goodbye!")


# ── Entry Point ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    run_subscriber()

