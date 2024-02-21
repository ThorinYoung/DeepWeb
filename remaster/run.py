import subprocess


def run(inputPath: str, refPath: str, UseGPU=False):
    if UseGPU:
        r = subprocess.run(["python", "remaster/remaster.py", "--input", inputPath, "--reference_dir", refPath, "--gpu"])
    else:
        r = subprocess.run(["python", "remaster/remaster.py", "--input", inputPath, "--reference_dir", refPath])
    return r


s1 = 'D:/Python workspace/DeepWeb/remaster/example/a-bomb_blast_effects_part.mp4'
s2 = 'D:/Python workspace/DeepWeb/remaster/example/references'
run(s1, s2, False)
