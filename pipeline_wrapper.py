import os
from datetime import datetime
from typing import List, Tuple
from text_extraction import preprocess_pod_transcript
from gpt_argument_mining import extract_arguments

class PipelineWrapper:
    def process_file(self, file_path: str) -> List[dict]:
        # Extract text from file
        text = preprocess_pod_transcript(file_path)

        # Extract arguments from text
        arguments = extract_arguments(text)

        # Run argument mining pipeline
        results = arguments###########

        # Add metadata to each result
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for result in results:
            result['timestamp'] = timestamp
            result['source_file'] = os.path.basename(file_path)

        # save the file
        output_filename = f"{os.path.basename(file_path)[:-4]}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        output_path = os.path.join('output', output_filename)
        with open(output_path, 'w') as f:
            json.dump(results, f)

        # Log successful processing
        self.log_processed_file(file_path)



        return results
