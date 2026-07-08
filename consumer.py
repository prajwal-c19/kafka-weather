from kafka import KafkaConsumer
import json
from collections import deque

# Create Kafka Consumer
consumer = KafkaConsumer(
    "weather-mangalore",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("Weather Consumer Started...\n")

# Store last readings
last_12 = deque(maxlen=12)   # 1 hour (12 × 5 min)
last_36 = deque(maxlen=36)   # 3 hours (36 × 5 min)

for message in consumer:
    weather = message.value

    print("\nNew Weather Data Received")
    print(weather)

    last_12.append(weather)
    last_36.append(weather)

    # -------- 1 Hour Average --------
    if len(last_12) == 12:
        avg_temp = sum(x["temperature"] for x in last_12) / 12
        avg_humidity = sum(x["humidity"] for x in last_12) / 12
        avg_pressure = sum(x["pressure"] for x in last_12) / 12

        print("\n===== 1 Hour Average =====")
        print(f"Temperature : {avg_temp:.2f} °C")
        print(f"Humidity    : {avg_humidity:.2f} %")
        print(f"Pressure    : {avg_pressure:.2f} hPa")

    # -------- 3 Hour Average --------
    if len(last_36) == 36:
        avg_temp = sum(x["temperature"] for x in last_36) / 36
        avg_humidity = sum(x["humidity"] for x in last_36) / 36
        avg_pressure = sum(x["pressure"] for x in last_36) / 36

        print("\n===== 3 Hour Average =====")
        print(f"Temperature : {avg_temp:.2f} °C")
        print(f"Humidity    : {avg_humidity:.2f} %")
        print(f"Pressure    : {avg_pressure:.2f} hPa")

    print("-" * 50)