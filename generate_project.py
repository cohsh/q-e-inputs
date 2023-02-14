import os

from qeinput.material import Material
from qeinput.inputs import SlurmJob, InputPWSCF


KEY = "Your API key of the Materials Project"

PWD = os.getcwd() + "/"
QE_DIR = "~/q-e/bin/"
PROJECT_DIR = "test/"
PSEUDO_DIR = PWD + "pseudos/local"
OUTDIR = "tmp/"

job = SlurmJob("PartitionName", 1, 128, 1)


def prepare_scf(mp_id: str):
    material = Material(KEY, mp_id)
    prefix = material.formula_pretty
    path = PROJECT_DIR + prefix + "/"

    if not os.path.exists(path):
        os.makedirs(path)

    input_scf = InputPWSCF(material, PSEUDO_DIR, OUTDIR, 60, [8, 8, 8])

    infile = prefix + ".scf.in"
    outfile = prefix + ".scf.out"
    input_scf.generate(path + infile)

    job.add_text("cd {dir}\n".format(dir=PWD+path))
    job.add_srun(QE_DIR + "pw.x", "", infile, outfile)
    job.add_text("\n")


def main():
    if not os.path.exists(PROJECT_DIR):
        os.makedirs(PROJECT_DIR)

    mp_ids = ["mp-149", "mp-2534"]

    for mp_id in mp_ids:
        prepare_scf(mp_id)

    job.generate(PROJECT_DIR + "job.sh")


if __name__ == "__main__":
    main()
