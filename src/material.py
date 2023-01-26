from mp_api.client import MPRester

import api

api_key = api.key


class Material:
    def __init__(self, material_id):
        with MPRester(api_key) as mpr:
            docs = mpr.summary.search(
                    material_ids=[material_id],
                    fields=["nsites", "nelements", "formula_pretty",
                            "structure", "is_metal",
                            "symmetry"]
                    )
        self.nsites = docs[0].nsites
        self.nelements = docs[0].nelements
        self.formula_pretty = docs[0].formula_pretty
        self.structure = docs[0].structure


Si = Material("mp-149")
print(Si.structure)
print(Si.structure.sites)
