# config/settings.py
APP_TITLE = "Dataset Visualizer"
APP_VERSION = "1.0.0"

# File upload settings (MB)
MAX_UPLOAD_SIZE_MB = 30

# Visualization settings
DEFAULT_CHART_TYPE = "line"
SUPPORTED_CHART_TYPES = ["line", "bar", "scatter", "histogram", "pie", "box", "heatmap"]

# Report settings
REPORT_FORMATS = ["PDF", "HTML"]

# Default dataset (for examples)
DEFAULT_DATASET = "data/sample1.csv"

# Theme settings (streamlit theme json already available in config/theme.json)
THEME_COLOR = "#1f77b4"
FONT_FAMILY = "Arial, sans-serif"
