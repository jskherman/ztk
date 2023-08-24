import datetime
import subprocess


def sync_notes():
    """
    Syncs the notes from the source path to the destination path.
    """
    source_path = r"E:\OneDrive\Documents\Basecamp\(P--) Personal\(PN-) Notes\(PN2) Current\(PN2 KN) Knowledge"
    destination_path = r"E:\OneDrive\Documents\Basecamp\(H--) Hobbies, Extracurriculars\(HA-) Code Playground\(HA2) Web Sites, Technologies\(HA2 PZ) Public Zettelkasten\content"

    command = f"rclone sync -P '{source_path}' '{destination_path}' --exclude-from exclude.txt"
    subprocess.run(
        ["powershell.exe", "-Command", command],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )

    assets_path = r"E:\OneDrive\Documents\Basecamp\(H--) Hobbies, Extracurriculars\(HA-) Code Playground\(HA2) Web Sites, Technologies\(HA2 PZ) Public Zettelkasten\content\001.assets\media"

    subprocess.run(
        [
            "powershell.exe",
            "-Command",
            f"rclone sync -P '{source_path}\\001.assets\\media' '{assets_path}'",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )


def commit_notes():
    """
    Commits and pushes the changes
    """
    # now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # command = f'git add docs/notes; git commit -m "Publish {now}"; git push'
    # subprocess.run(
    #     ["powershell.exe", "-Command", command],
    #     stdout=subprocess.PIPE,
    #     stderr=subprocess.STDOUT,
    # )

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Check if there are any changes in the 'docs/notes' directory using 'git status'
    status_output = subprocess.run(
        ["git", "status", "--porcelain", "content"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True,
    )

    if status_output.stdout.strip():
        # If there are changes, proceed with commit and push
        command = f'git add content; git commit -m "Publish {now}"; git push'
        subprocess.run(
            ["powershell.exe", "-Command", command],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=True,
        )
    else:
        print("No changes in 'content' directory. Skipping commit and push.")


def main():
    sync_notes()
    # commit_notes()


if __name__ == "__main__":
    main()
