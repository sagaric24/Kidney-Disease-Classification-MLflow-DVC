#return type of data ingestion
from dataclasses import dataclass
from pathlib import Path

#everything that is mentioned in config.yaml for data ingestion
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path