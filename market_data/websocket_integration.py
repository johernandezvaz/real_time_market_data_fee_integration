# market_data/websocket_integration.py
import asyncio
import websockets
import json
from market_data.models import MarketData

async def connect_to_websocket():
    route = 'quotes/price'
    uri = "wss://ws.twelvedata.com/v1/{$route}?apikey=e89765d6ab7d45efb0f7ee7e3b832b02"

    async with websockets.connect(uri) as websocket:
        while True:
            data = await websocket.recv()
            await process_data(data)

async def process_data(data):
    # Parse data as JSON
    data_dict = json.loads(data)
    
    # Print the received data
    print(data_dict)

    # Extract relevant information from the received data
    timestamp = data_dict.get('timestamp', '')
    symbol = data_dict.get('symbol', '')
    price = data_dict.get('price', '')
    exchange_name = data_dict.get('exchange', '')

    # Save the extracted information to the database
    MarketData.objects.create(
        timestamp=timestamp,
        symbol=symbol,
        price=price,
        exchange=exchange_name
    )


# Run the event loop
asyncio.get_event_loop().run_until_complete(connect_to_websocket())
