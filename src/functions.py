import os
from datetime import datetime


def create_ascii_progress(trial_id, current_epoch, total_epochs, parameters, loss=None, path='./'):
    """Create a simple ASCII progress bar and save to text file"""
    progress_percent = (current_epoch / total_epochs) * 100
    bar_length = 50
    filled_length = int(bar_length * current_epoch // total_epochs)
    
    bar = '█' * filled_length + '░' * (bar_length - filled_length)
    
    progress_text = f"Trial {trial_id}: [{bar}] {progress_percent:.1f}% ({current_epoch}/{total_epochs})"
    if loss is not None:
        progress_text += f" | Loss: {loss:.6f}"
    
    # Create directory if it doesn't exist
    os.makedirs(path, exist_ok=True)
    
    # Save to individual trial progress file in specified path
    file_path = os.path.join(path, f'trial_{trial_id}_progress.txt')
    with open(file_path, 'w') as f:
        f.write(progress_text + '\n')
        f.write(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Current parameters: {parameters}\n")