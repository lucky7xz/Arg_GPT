import os
import json
from datetime import datetime
from pipeline_wrapper import PipelineWrapper

if __name__ == '__main__':
    # Set up pipeline
    pipeline = PipelineWrapper()

    # Define input and output directories
    input_dir = 'path/to/input/directory'
    output_dir = 'path/to/output/directory'

    # Loop through files in input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(input_dir, filename)

            # Run pipeline on file
            result = pipeline.process_file(file_path)

            # Save output to JSON file with appropriate metadata
            output_filename = f"{filename[:-4]}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            output_path = os.path.join(output_dir, output_filename)
            with open(output_path, 'w') as f:
                metadata = {
                    'input_file': file_path,
                    'output_file': output_path,
                    'extraction_timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'instruction_prompt': 'Your instruction prompt here'
                }
                json.dump({'metadata': metadata, 'result': result}, f)

            # Log successful processing
            pipeline.log_processed_file(file_path)
        else:
            continue