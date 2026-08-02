import httpx
import asyncio


async def fetch_todo(todo_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://jsonplaceholder.typicode.com/todos/{todo_id}")
        return response.json()

async def main():
    todos = await asyncio.gather(fetch_todo(1), fetch_todo(2), fetch_todo(3), fetch_todo(4))
    print(todos)

asyncio.run(main())
