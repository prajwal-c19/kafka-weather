from kafka import KafkaProducer
import json
import time
from weather_api import get_weather

# Create Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

TOPIC = "weather-mangalore"

print("Weather Producer Started...")

while True:
    weather = get_weather()

    if weather:
        producer.send(TOPIC, weather)
        producer.flush()

        print("Weather Sent:")
        print(weather)
        print("-" * 50)

    # Wait for 5 minutes
    time.sleep(300)