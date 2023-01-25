import pandas as pd
from mp_api.client import MPRester

import api

api_key = api.key

with MPRester(api_key) as mpr:
    docs = mpr.summary.search(material_ids=["mp-149"], fields=["structure"])
    structure = docs[0].structure

print(structure)
