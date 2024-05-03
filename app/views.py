from rest_framework.views import APIView
from rest_framework.response import Response
from .celery_tasks import predict_task
from .serializers import PredictSerializer, PredictionResultSerializer

class PredictView(APIView):

    serializer_class = PredictSerializer

    def post(self, request, *args, **kwargs):
        print(request.headers)

        # get and validate input
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        model_input = serializer.validated_data.get("model_input")
        async_mode = serializer.validated_data.get("async_mode", False)
        print(f"async_mode: {async_mode}")

        if async_mode:
            print("Predicting Asynchronously..")
            task = predict_task.delay(model_input)  # .delay() to make prediction run asynchronously
            return Response({
                "message": "Asynchronous prediction started.",
                "task_id": task.id,
            })
        
        else:
            print("Predicting Synchronously...")
            prediction = predict_task(model_input)  # synchronous call
            print("Predicted")
            print(f"Response: {prediction}")
            return Response({
                "input": model_input, 
                "prediction": prediction
            })
    

    def get(self, request, *args, **kwargs):
        return Response({
            "message": "Usage: send post request with model_input (Any) and optionally async_mode (bool) params.",

        })
    

class PredictionResultView(APIView):
    serializer_class = PredictionResultSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=kwargs)
        print(serializer.is_valid(raise_exception=True))
        print("Getting async prediction result")
        prediction_id = kwargs.get("prediction_id")
        task = predict_task.AsyncResult(prediction_id)
        return Response({
            "prediction_id": prediction_id,
            "task_status": task.status,
            "task_result": task.result
        })
