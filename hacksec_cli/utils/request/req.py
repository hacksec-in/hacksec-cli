import json
import httpx
import asyncio


class MakeRequest():
    """make http request to our server"""

    def __init__(self, config):
        self.host = config.host
        self.header = {
            "Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br"}
        self.session = httpx.AsyncClient(base_url=self.host)

    def runner(func):
        """runner"""
        def wrapper(*args, **kwargs):
            loop = asyncio.get_event_loop()
            response = loop.run_until_complete(func(*args, **kwargs))
            return response
        return wrapper

    def authenticate(self, access_token):
        """authenticate to our server"""
        self.header["Authorization"] = "Bearer " + access_token

    @runner
    async def close_session(self):
        """close session"""
        await self.session.aclose()

    @runner
    async def get(self, endpoint):
        """make get request"""
        response = await self.session.get(endpoint, headers=self.header)
        return response.json(), response.status_code

    @runner
    async def post(self, endpoint, payload):
        """make post request"""
        response = await self.session.post(endpoint, data=json.dumps(payload), headers=self.header)
        return response.json(), response.status_code

    @runner
    async def upload(self, endpoint, file):
        """make post request"""
        files = {'file': file}
        response = await self.session.post(self.host + endpoint, files=files, headers=self.header)
        return response.json(), response.status_code
