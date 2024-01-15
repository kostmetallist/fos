import asyncio
from time import perf_counter


async def say_delayed(message, delay):
    await asyncio.sleep(delay)
    print(message)


async def main():
    async with asyncio.TaskGroup() as tg:
        task_1 = tg.create_task(
            say_delayed('hello', 1)
        )
        
        task_2 = tg.create_task(
            say_delayed('world', 2)
        )

        print(f'Started at {perf_counter():6f}')
        # Automatically awaits on all tasks once exited from the context manager

    print(f'Completed at {perf_counter():6f}')


if __name__ == '__main__':
    asyncio.run(main())
