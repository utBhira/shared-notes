import subprocess


staging_is_equal_to_origin = subprocess.run(
    "git diff staging/main origin/main",
    shell=True,
    text=True,
    check=True,
    # capture_output=True
)





