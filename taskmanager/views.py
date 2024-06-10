# taskmanager/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import scrape_coin_data
from .models import Job, Task
from django.shortcuts import get_object_or_404

class StartScrapingView(APIView):
    def post(self, request):
        # Validate input data
        coins = request.data.get('coins', [])
        if not isinstance(coins, list):
            return Response({'error': 'Invalid input. Expected a list of coin acronyms.'}, status=status.HTTP_400_BAD_REQUEST)

        job = Job.objects.create(coins=coins)
      

         # Generate a unique job ID
        for coin in coins:
            scrape_coin_data.delay(job.job_id, coin)
            
        
            

        return Response({'job_id': job.job_id}, status=status.HTTP_202_ACCEPTED)

class ScrapingStatusView(APIView):
    def get(self, request, job_id):
        # Query the database for the Job and associated Tasks
        job = get_object_or_404(Job, job_id=job_id)
        tasks = Task.objects.filter(job_id=job_id)

        # Format the scraped data for each coin
        scraped_data = []
        for task in tasks:
            coin_data = {
                'coin': task.coin_name,
                'output': {
                    'price': task.price,
                    'price_change': task.price_change,
                    'market_cap': task.market_cap,
                    'market_cap_rank': task.market_cap_rank,
                    'volume': task.volume,
                    'volume_rank': task.volume_rank,
                    'volume_change': task.volume_change,
                    'circulating_supply': task.circulating_supply,
                    'total_supply': task.total_supply,
                    'diluted_market_cap': task.diluted_market_cap,
                    # Add more fields as necessary
                }
            }
            scraped_data.append(coin_data)

        # Return the scraped data in JSON format
        return Response({'job_id': job_id, 'tasks': scraped_data}, status=status.HTTP_200_OK)
