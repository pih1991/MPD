import os
import requests

def download_pdb(pdb_id, output_dir='.'):
    """
    Download a PDB file given its ID.
    
    :param pdb_id: The 4-character PDB ID
    :param output_dir: Directory to save the file (default is current directory)
    """
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
    response = requests.get(url)
    
    if response.status_code == 200:
        filename = os.path.join(output_dir, f"{pdb_id}.pdb")
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Successfully downloaded {pdb_id}")
    else:
        print(f"Failed to download {pdb_id}. Status code: {response.status_code}")

def main():
    # List of PDB IDs you want to download
    pdb_ids = ['3EGM', '7SGE', '3VDX', '4NVN', '6OT9', '4EGG', '2LV8', '3VJF', '7R5K', '6O07', '5CSL', '7A1G', '5M5W', '8EOV', '8GA9', '8GAA', '8GAQ', '8UB3', '8UAO', '8UBG', '8T6C', '8T6N', '8T6E', '8UZL', '6VFH', '6VFI', '6VFJ', '6UTK', '5KP9', '6V8X', '6VKN', '6VL5', '6VL6', '6VFK', '5CY5', '7KNA', '6P6F', '7SCN', '8UR5', '8UR7', '8DO3', '8DO4', '8DO5', '8DO6', '8DO7', '8DO8', '8DO9']  # Replace with your desired PDB IDs
    
    # Create a directory to store the PDB files
    output_dir = 'pdb_files'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Download each PDB file
    for pdb_id in pdb_ids:
        download_pdb(pdb_id, output_dir)

if __name__ == "__main__":
    main()