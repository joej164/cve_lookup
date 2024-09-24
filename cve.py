import subprocess
import shutil
import json
from pathlib import Path


class CVE:
    def __init__(self):
        self.REPO_URL = "https://github.com/CVEProject/cvelistV5.git"
        self.REPO_DIR = Path("./cvelistV5")
        self.CVE_PATH = self.REPO_DIR / "cves"
        self.get_cve_list()
        self.read_cves_into_tree()

    def get_cve_list(self):
        if self.REPO_DIR.exists() and any(self.REPO_DIR.iterdir()):
            print("Repo already exists")
        else:
            print(f"Pulling repo: {self.REPO_DIR}")
            subprocess.run(
                ["git", "clone", "--depth=1", self.REPO_URL]
            )  # Doing a shallow clone as all we care about is the data

    def remove_cve_list(self):
        if self.REPO_DIR.exists():
            shutil.rmtree(self.REPO_DIR)
            print(f"Deleted directory {self.REPO_DIR}")
        else:
            print(
                f"Unable to delete directory {self.REPO_DIR}.  Directory does not exist."
            )

    def read_cves_into_tree(self, years=None):
        years = ["2024"]

        for year in years:
            directory = self.CVE_PATH / year

            for file in directory.iterdir():
                for f in file.iterdir():
                    with open(f) as jsonfile:
                        out = json.load(jsonfile)
                        print(out)
                        print("*" * 100)
                break


a = CVE()
