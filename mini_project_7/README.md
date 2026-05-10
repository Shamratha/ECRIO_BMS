# Mini Project 7 — MQTT Publisher & Subscriber 📡

A beginner-friendly demonstration of the **MQTT protocol** using Python's
`paho-mqtt` library and the free public broker `test.mosquitto.org`.

---

## 📁 Structure
```
mini_project_7/
├── publisher.py      ← Sends random messages every 3 seconds
├── subscriber.py     ← Listens and prints received messages
├── README.md
├── requirements.txt
└── sample_output.txt
```

---

## 🧠 What is MQTT?

**MQTT** (Message Queuing Telemetry Transport) is a lightweight
publish-subscribe messaging protocol widely used in **IoT** (Internet of Things).

```
Publisher  ──publishes──►  Broker  ──delivers──►  Subscriber
(publisher.py)         (test.mosquitto.org)      (subscriber.py)
```

| Term | Meaning |
|------|---------|
| **Broker** | Server that routes messages (like a post office) |
| **Publisher** | Client that sends messages to a topic |
| **Subscriber** | Client that receives messages from a topic |
| **Topic** | Address/channel for messages (`ecrio/bms/messages`) |
| **QoS 0** | Fire and forget — no acknowledgement |
| **QoS 1** | At least once — broker acknowledges delivery |
| **QoS 2** | Exactly once — guaranteed single delivery |

---

## ▶️ Setup & Run

### 1 — Install dependency
```bash
cd mini_project_7
pip install -r requirements.txt
```

### 2 — Open TWO terminals

**Terminal 1 — Start subscriber FIRST:**
```bash
cd mini_project_7
python subscriber.py
```

**Terminal 2 — Start publisher:**
```bash
cd mini_project_7
python publisher.py
```

You will see messages appear in Terminal 1 every 3 seconds!

---

## ⚙️ Configuration

Both scripts share these settings (edit at the top of each file):

| Setting | Value | Description |
|---------|-------|-------------|
| `BROKER` | `test.mosquitto.org` | Free public broker |
| `PORT` | `1883` | Default MQTT port |
| `TOPIC` | `ecrio/bms/messages` | Custom topic name |
| `QOS` | `1` | At-least-once delivery |
| `INTERVAL` | `3` | Seconds between publishes |

---

## 🛑 Stopping

Press `Ctrl+C` in either terminal to stop gracefully.

---

## 🖼 Screenshot Placeholder
> _Add a screenshot here_

![MP7 Screenshot](../screenshots/mp7_screenshot.png)

---

## 📦 Dependencies
```
paho-mqtt>=2.0.0
```
