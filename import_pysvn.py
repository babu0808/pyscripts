import subprocess

def svn_checkout(repo_url, destination_path, username, password):
    # Full path to SVN executable (optional, only if not in PATH)
    svn_executable = "svn"  # Change to the full path to svn.exe if necessary

    # SVN checkout command with authentication
    cmd = [
        svn_executable, 
        "checkout", 
        repo_url, 
        destination_path, 
        "--username", username, 
        "--password", password, 
        "--non-interactive",  # Prevent interactive prompts
        "--trust-server-cert"  # Trust server certificate (if required)
    ]

    try:
        # Execute the SVN command
        result = subprocess.run(cmd, capture_output=True, text=True)

        # Check the result
        if result.returncode == 0:
            print(f"Checked out successfully to {destination_path}")
        else:
            print(f"Error: {result.stderr}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    repo_url = "http://wush.net/svn/bcits/Projects/BsmartIOT/AMR_EC200"
    destination_path = r"D:\svn\AMR_EC200"
    username = "babu.malagaveli@bcits.in"
    password = "Babu@123"

    svn_checkout(repo_url, destination_path, username, password)
