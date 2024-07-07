import subprocess
import sys
from IPython.display import clear_output

def install_and_import(package_name):
    try:
        # Try to import the package
        __import__(package_name)
        print(f"{package_name} is already installed.")
    except ImportError:
        # If not installed, attempt to install the package
        try:
            print(f"Installing {package_name} library not by default in Colab")
            result = subprocess.run([sys.executable, "-m", "pip", "install", package_name], capture_output=True, text=True)
            # If the installation is successful, clear the partial output and show the final message
            if result.returncode == 0:
                clear_output(wait=True)
                print(f"Successfully installed {package_name}")
                __import__(package_name)
            else:
                # If there's an error, print the full output
                print(result.stdout)
                print(result.stderr)
        except Exception as e:
            print(f"An error occurred during installation: {e}")

# How to call it
# install_and_import('pandas_ta')
