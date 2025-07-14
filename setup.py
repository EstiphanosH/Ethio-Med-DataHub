import os
import sys
from pathlib import Path

def create_file(path, content=""):
    """Safely create a file with content."""
    try:
        dir_name = os.path.dirname(path)
        if dir_name:  # Only create directory if path is not root
            os.makedirs(dir_name, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return 1  # Count created file
    except Exception as e:
        print(f"Error creating {path}: {str(e)}")
        sys.exit(1)

def create_repo_structure():
    """Create the complete production-ready structure in current directory."""
    files_created = 0

    # Create directories with .gitkeep files
    directories = [
        ".github/workflows",
        "data/processed",
        "data/raw",
        "docker/initdb",
        "docs",
        "logs",
        "scripts",
        "src/api",
        "src/dagster",
        "src/dbt_project/dbt_internal_packages",
        "src/dbt_project/dbt_packages",
        "src/dbt_project/logs",
        "src/dbt_project/macros",
        "src/dbt_project/models",
        "src/dbt_project/target",
        "src/dbt_project/tests",
        "src/scraper/__pycache__",
        "src/yolo",
        "tests",
    ]

    for dir_path in directories:
        os.makedirs(dir_path, exist_ok=True)
        # Create .gitkeep file
        gitkeep_path = os.path.join(dir_path, ".gitkeep")
        Path(gitkeep_path).touch()
        files_created += 1  # Count .gitkeep files

    # Create files with initial content
    files = {
        # Docker files
        "docker/docker-compose.db.yml": "# Database-specific compose config",
        "docker/docker-compose.yml": "# Main docker compose config",
        "docker/Dockerfile": "# Base Dockerfile",
        "docker/Dockerfile.api": "# API Dockerfile",
        "docker/Dockerfile.db": "# Database Dockerfile",
        "docker/Dockerfile.cli": "# CLI Dockerfile",
        "docker/Dockerfile.scraper": "# Scraper Dockerfile",
        
        # Scripts
        "scripts/start-db.sh": "#!/bin/bash\ndocker-compose -f docker/docker-compose.db.yml up -d",
        
        # API files
        "src/api/crud.py": "# CRUD operations for API",
        "src/api/database.py": "# Database connection setup",
        "src/api/main.py": "# FastAPI main entry",
        "src/api/models.py": "# SQLAlchemy models",
        "src/api/schemas.py": "# Pydantic schemas",
        
        # Dagster files
        "src/dagster/pipeline.py": "# Dagster pipeline definition",
        "src/dagster/schedule.py": "# Dagster schedule configuration",
        
        # dbt files
        "src/dbt_project/dbt_project.yml": "# dbt project configuration",
        "src/dbt_project/load_raw_data.py": "# Script to load raw data to PostgreSQL",
        "src/dbt_project/package-lock.json": "{}",
        "src/dbt_project/packages.yml": "# dbt packages configuration",
        "src/dbt_project/profiles.yml": "# dbt profiles configuration",
        "src/dbt_project/user.yml": "# User configuration",
        
        # Scraper files
        "src/scraper/scheduler.py": "# Scraping scheduler",
        "src/scraper/telegram_scraper.py": "# Telegram scraper implementation",
        "src/scraper/utils.py": "# Utility functions for scraper",
        
        # YOLO file
        "src/yolo/yolo_object_detection.py": "# YOLO object detection implementation",
        
        # Root files
        ".env.example": "# Environment variables template",
        ".gitignore": "*.pyc\n__pycache__/\n.env\n.venv/\n.DS_Store\n.idea/\n.vscode/\n\n# Data files\ndata/raw/\ndata/processed/\n\n# Logs\nlogs/\n\n# dbt artifacts\nsrc/dbt_project/target/\n",
        "README.md": "# Ethiopian Medical Insights Project\n\n## Overview\n\nEnd-to-end data pipeline for Telegram medical data analysis",
        "requirements.txt": "# Python dependencies",
    }

    for path, content in files.items():
        files_created += create_file(path, content)

    print("\n✅ Project structure created successfully!")
    print(f"→ Created {len(directories)} directories")
    print(f"→ Generated {files_created} files")
    print("\nNext steps:")
    print("1. Fill in the .env.example file and rename to .env")
    print("2. Add Telegram API credentials to .env")
    print("3. Customize dbt_project.yml and profiles.yml")
    print("4. Run 'pip install -r requirements.txt' to install dependencies")
    print("5. Start development with 'docker-compose up -d'")

if __name__ == "__main__":
    try:
        create_repo_structure()
    except Exception as e:
        print(f"\n❌ Setup failed: {str(e)}")
        sys.exit(1)