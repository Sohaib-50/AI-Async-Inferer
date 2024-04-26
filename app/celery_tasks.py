from celery import shared_task
import time
import random

@shared_task
def predict_task(model_input):
    print("Predicting...")
    time.sleep(random.randint(8, 15))  # Simulate processing delay
    result = str(random.randint(100, 10000))
    return result 