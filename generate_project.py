import os

from qeinput.material import Material
from qeinput.inputs import SlurmJob, InputPWSCF, InputPWNSCF


KEY = "Your API key of the Materials Project"

PWD = os.getcwd() + "/"
QE_DIR = "~/q-e/bin/"
PROJECT_DIR = "test/"
PSEUDO_DIR = PWD + "pseudos/local"
OUTDIR = "tmp/"

job = SlurmJob("PartitionName", 1, 128, 1)


def prepare_scf(material: Material, ecutwfc: int, k_points: list):
    prefix = material.formula_pretty
    path = PROJECT_DIR + prefix + "/"

    if not os.path.exists(path):
        os.makedirs(path)

    input_scf = InputPWSCF(material, PSEUDO_DIR, OUTDIR, ecutwfc, k_points)

    infile = prefix + ".pw.scf.in"
    outfile = prefix + ".pw.scf.out"
    input_scf.generate(path + infile)

    job.add_text("cd {dir}\n".format(dir=PWD+path))
    job.add_srun(QE_DIR + "pw.x", "", infile, outfile)
    job.add_text("\n")


def prepare_nscf(material: Material, ecutwfc: int, k_points: list, nbnd: int):
    prefix = material.formula_pretty
    path = PROJECT_DIR + prefix + "/"

    if not os.path.exists(path):
        os.makedirs(path)

    input_nscf = InputPWNSCF(material, PSEUDO_DIR, OUTDIR, ecutwfc,
                             k_points, nbnd)

    infile = prefix + ".pw.nscf.in"
    outfile = prefix + ".pw.nscf.out"
    input_nscf.generate(path + infile)

    job.add_text("cd {dir}\n".format(dir=PWD+path))
    job.add_srun(QE_DIR + "pw.x", "", infile, outfile)
    job.add_text("\n")


def main():
    if not os.path.exists(PROJECT_DIR):
        os.makedirs(PROJECT_DIR)

    mp_ids = ["mp-149", "mp-2534"]

    for mp_id in mp_ids:
        material = Material(KEY, mp_id)
        prepare_scf(material, 60, [8, 8, 8])
        prepare_nscf(material, 60, [[0.0, 0.0, 0.0]], 10)

    job.generate(PROJECT_DIR + "job.sh")


if __name__ == "__main__":
    main()
