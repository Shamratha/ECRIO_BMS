"""
publisher.py — ECRIO_BMS Mini Project 7
─────────────────────────────────────────
MQTT Publisher Script.

What this does:
  1. Connects to a public MQTT broker (broker.emqx.io)
  2. Publishes a random message to the topic "ecrio/bms/messages"
     every 3 seconds
  3. Logs every action with a timestamp
  4. Handles connection errors gracefully

MQTT Concept:
  Publisher  →  Broker  →  Subscriber
  (this file)   (server)   (subscriber.py)

Run in Terminal 1:
    python publisher.py

Make sure subscriber.py is running in Terminal 2 first!
"""

import paho.mqtt.client as mqtt
import time
import random
import logging
from datetime import datetime

# ── Logging Setup ──────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("MQTT-Publisher")

# ── MQTT Configuration ─────────────────────────────────────────────────────────
BROKER   = "broker.emqx.io"   # free public broker — no signup needed
PORT     = 1883                   # default unencrypted MQTT port
TOPIC    = "ecrio/bms/messages"   # custom topic name for this project
QOS      = 1                      # Quality of Service 1 = at least once delivery
INTERVAL = 3                      # seconds between messages

# ── Random message pool ────────────────────────────────────────────────────────
MESSAGES = [
    "Hello from ECRIO_BMS Publisher! 🚀",
    "MQTT is a lightweight publish-subscribe protocol.",
    "Python + paho-mqtt makes IoT easy!",
    "Sending data from publisher to subscriber.",
    "Real-time messaging with MQTT broker.",
    "ECRIO_BMS Mini Project 7 — running!",
    "Temperature: {:.1f}°C".format(random.uniform(20, 40)),
    "Humidity: {:.1f}%".format(random.uniform(40, 90)),
    "Device status: ONLINE ✅",
    "Heartbeat ping from publisher.",
]


# ── Callback Functions ─────────────────────────────────────────────────────────
# paho-mqtt calls these functions automatically on specific events.

def on_connect(client, userdata, flags, reason_code, properties=None):
    """Called when the client connects to the broker."""
    if reason_code == 0:
        logger.info(f"✅  Connected to broker: {BROKER}:{PORT}")
        logger.info(f"📤  Publishing to topic: '{TOPIC}'")
        logger.info("─" * 55)
    else:
        logger.error(f"❌  Connection failed. Reason code: {reason_code}")


def on_publish(client, userdata, mid, reason_code=None, properties=None):
    """Called when a message is successfully published."""
    logger.debug(f"Message {mid} acknowledged by broker.")


def on_disconnect(client, userdata, disconnect_flags, reason_code=None, properties=None):
    """Called when the client disconnects from the broker."""
    logger.warning(f"⚠️  Disconnected from broker. Reason code: {reason_code}")


# ── Main Publisher Logic ───────────────────────────────────────────────────────

def build_payload(message: str) -> str:
    """
    Wrap the message with a timestamp so the subscriber
    can see exactly when it was sent.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{timestamp}] {message}"


def run_publisher():
    """Create MQTT client, connect to broker, and publish messages in a loop."""

    # ── Create client instance ────────────────────────────────────────────────
    # CallbackAPIVersion.VERSION2 is required for paho-mqtt >= 2.0
    client = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2,
        client_id="ecrio_bms_publisher",
    )

    # ── Attach callbacks ──────────────────────────────────────────────────────
    client.on_connect    = on_connect
    client.on_publish    = on_publish
    client.on_disconnect = on_disconnect

    print("\n" + "=" * 55)
    print("  📡  ECRIO_BMS MQTT Publisher")
    print(f"  Broker : {BROKER}:{PORT}")
    print(f"  Topic  : {TOPIC}")
    print(f"  Interval: every {INTERVAL} seconds")
    print("=" * 55 + "\n")

    # ── Connect to broker ─────────────────────────────────────────────────────
    try:
        logger.info(f"Connecting to {BROKER}:{PORT} ...")
        client.connect(BROKER, PORT, keepalive=60)
    except Exception as exc:
        logger.error(f"Could not connect to broker: {exc}")
        logger.error("Check your internet connection and try again.")
        return

    # ── Start background network thread ───────────────────────────────────────
    # loop_start() handles reconnections and ACKs in the background
    client.loop_start()

    # ── Wait for connection to establish ──────────────────────────────────────
    time.sleep(1.5)

    msg_count = 0
    logger.info("Starting to publish. Press Ctrl+C to stop.\n")

    try:
        while True:
            # Pick a random message from the pool
            message = random.choice(MESSAGES)
            payload = build_payload(message)

            # Publish to the broker
            result = client.publish(TOPIC, payload, qos=QOS)

            msg_count += 1
            logger.info(f"[MSG #{msg_count}] Published → {payload}")

            # Wait before sending the next message
            time.sleep(INTERVAL)

    except KeyboardInterrupt:
        logger.info(f"\n🛑  Publisher stopped by user after {msg_count} message(s).")

    finally:
        client.loop_stop()
        client.disconnect()
        logger.info("Disconnected cleanly. Goodbye!")


# ── Entry Point ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    run_publisher()

