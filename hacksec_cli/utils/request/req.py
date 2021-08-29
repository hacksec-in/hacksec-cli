import aiohttp
import asyncio


class MakeRequest():
    """make http request to our server"""

    def __init__(self, config):
        connector = aiohttp.TCPConnector(limit=50, force_close=True)
        self.host = config.host
        self.header = {
            "Accept": "application/json, text/plain, */*", "Connection": "keep-alive", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "hacksec cli/"+config.version}
        self.session = aiohttp.ClientSession(
            trust_env=True, connector=connector)

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
        await self.session.close()

    @runner
    async def get(self, endpoint):
        """make get request"""
        async with self.session.get(self.host + endpoint, headers=self.header) as response:
            return await response.json(), response.status

    @runner
    async def post(self, endpoint, payload):
        """make post request"""
        async with self.session.post(self.host + endpoint, json=payload, headers=self.header) as response:
            return await response.json(), response.status

    @runner
    async def upload(self, endpoint, file):
        """make post request"""
        form = aiohttp.FormData()
        form.add_field('file', file)
        async with self.session.post(self.host + endpoint, data=form, headers=self.header) as response:
            return await response.json(), response.status
