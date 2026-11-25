import json
import subprocess
from pprint import pprint
from shlex import quote


# NOTE: TEST
# with open("./gh-data.json", "r", encoding="utf-8") as file:
#     data = sorted(json.load(file), key=lambda pr: pr["createdAt"])
# Change this to be dynamic file

subprocess.run("git fetch --all", shell=True)
# but now we would also have to checks whether the pr is updated or not.
# and if there's no update after our last operation i don't think that we really
# have to do anything about it.

# if there's a change what should have happened is that it should
# git switch staging/main
# git reset --hard orign


with open("gh_pr_list.json", "w", encoding="utf-8") as file:
    gh_pr_list = json.dump(
        json.loads(
            subprocess.run(
                "gh pr list --json createdAt,baseRefName,headRefName,title",
                shell=True,
                text=True,
                check=True,
                capture_output=True
            ).stdout
        ),
        file,
        ensure_ascii=False,
        indent=2
    )

with open("./gh_pr_list.json", "r", encoding="utf-8") as file:
    data = sorted(json.load(file), key=lambda pr: pr["createdAt"])


def collect_prs(base):
    result = []
    index = 0

    while index < len(data):
        pr = data[index]
        index += 1

        if pr["baseRefName"] == base:
            result.append(pr["headRefName"])
            result.extend(collect_prs(pr["headRefName"]))

    # Base case: no PR targets this base, so result is [].
    return result


branches = collect_prs("main")

for i in range(len(branches)):
    branch = branches[i]
    print(branch)
    previous = "main" if i == 0 else branches[i - 1]

    print(f"git switch {quote(branch)}")
    print(f"git rebase {quote(previous)}")
    print(f"git switch qa/main")



