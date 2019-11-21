import faust

#
# TODO: Create the faust app with a name and broker
#
app = faust.App("hello-world-faust", broker="localhost:9092")

#
# TODO: Connect Faust to a topic
#
topic = app.topic("com.udacity.streams.clickevents")

#
# TODO: Provide an app agent to execute this function on topic event retrieval
#
@app.agent(topic)
async def clickevent(clickevents):
    async for ce in clickevents:
        print(ce)


if __name__ == "__main__":
    app.main()

## python exercise6.1.solution.y worker
#┌ƒaµS† v1.7.4─┬───────────────────────────────────────────┐
#│ id          │ hello-world-faust                         │
#│ transport   │ [URL('kafka://localhost:9092')]           │
#│ store       │ memory:                                   │
#│ web         │ http://localhost:6066/                    │
#│ log         │ -stderr- (warn)                           │
#│ pid         │ 829                                       │
#│ hostname    │ 55d7c7428e44                              │
#│ platform    │ CPython 3.7.3 (Linux x86_64)              │
#│ drivers     │                                           │
#│   transport │ aiokafka=1.0.6                            │
#│   web       │ aiohttp=3.6.2                             │
#│ datadir     │ /home/workspace/hello-world-faust-data    │
#│ appdir      │ /home/workspace/hello-world-faust-data/v1 │
#└─────────────┴───────────────────────────────────────────┘
#starting➢ 🌖 🌘 -INT- -INT- -INT- -INT- -INT- -INT-
