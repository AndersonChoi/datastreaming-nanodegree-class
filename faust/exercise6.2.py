from dataclasses import asdict, dataclass
import json

import faust


#
# TODO: Define a ClickEvent Record Class
#
@dataclass
class ClickEvent(faust.Record):
    email: str
    timestamp: str
    uri: str
    number: int

app = faust.App("sample2", broker="kafka://localhost:9092")

#
# TODO: Provide the key and value type to the clickevent
#
clickevents_topic = app.topic(
    "com.udacity.streams.clickevents",
    key_type=str,
    value_type=ClickEvent,
)

@app.agent(clickevents_topic)
async def clickevent(clickevents):
    async for ce in clickevents:
        print(json.dumps(asdict(ce), indent=2))


if __name__ == "__main__":
    app.main()

#root@37513b2a4460:/home/workspace# python exercise6.2.solution.py worker
#┌ƒaµS† v1.7.4─┬──────────────────────────────────────────┐
#│ id          │ sample2                                  │
#│ transport   │ [URL('kafka://localhost:9092')]          │
#│ store       │ memory:                                  │
#│ web         │ http://localhost:6066/                   │
#│ log         │ -stderr- (warn)                          │
#│ pid         │ 827                                      │
#│ hostname    │ 37513b2a4460                             │
#│ platform    │ CPython 3.7.3 (Linux x86_64)             │
#│ drivers     │                                          │
#│   transport │ aiokafka=1.0.6                           │
#│   web       │ aiohttp=3.6.2                            │
#│ datadir     │ /home/workspace/sample2-data             │
#│ appdir      │ /home/workspace/sample2-data/v1          │
#└─────────────┴──────────────────────────────────────────┘
#starting➢ •
# 😊
#[2019-11-21 07:36:15,673: WARNING]: {
#  "email": "erinlong@gibson.com",
#  "timestamp": "1973-10-04T17:16:58",
#  "uri": "http://www.king-brooks.info/login/",
#  "number": 859
#} 
#[2019-11-21 07:36:15,674: WARNING]: {
#  "email": "andreamonroe@yahoo.com",
#  "timestamp": "1970-02-28T11:41:47",
#  "uri": "http://www.wilson.net/categories/wp-content/terms.asp",
#  "number": 965
#} 
